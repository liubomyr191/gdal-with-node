#include "gdal_common.hpp"
#include "gdal_majorobject.hpp"
#include "gdal_dataset.hpp"
#include "gdal_rasterband.hpp"
#include "gdal_driver.hpp"
#include "gdal_spatial_reference.hpp"
#include "gdal_layer.hpp"
#include "gdal_geometry.hpp"
#include "collections/dataset_bands.hpp"
#include "collections/dataset_layers.hpp"

namespace node_gdal {

Persistent<FunctionTemplate> Dataset::constructor;
ObjectCache<GDALDataset, Dataset> Dataset::dataset_cache;
ObjectCache<OGRDataSource, Dataset> Dataset::datasource_cache;

void Dataset::Initialize(Handle<Object> target)
{
	NanScope();

	Local<FunctionTemplate> lcons = NanNew<FunctionTemplate>(Dataset::New);
	lcons->InstanceTemplate()->SetInternalFieldCount(1);
	lcons->SetClassName(NanNew("Dataset"));

	NODE_SET_PROTOTYPE_METHOD(lcons, "toString", toString);
	NODE_SET_PROTOTYPE_METHOD(lcons, "setGCPs", setGCPs);
	NODE_SET_PROTOTYPE_METHOD(lcons, "getGCPs", getGCPs);
	NODE_SET_PROTOTYPE_METHOD(lcons, "getGCPProjection", getGCPProjection);
	NODE_SET_PROTOTYPE_METHOD(lcons, "getFileList", getFileList);
	NODE_SET_PROTOTYPE_METHOD(lcons, "flush", flush);
	NODE_SET_PROTOTYPE_METHOD(lcons, "close", close);
	NODE_SET_PROTOTYPE_METHOD(lcons, "getMetadata", getMetadata);
	NODE_SET_PROTOTYPE_METHOD(lcons, "testCapability", testCapability);
	NODE_SET_PROTOTYPE_METHOD(lcons, "executeSQL", executeSQL);
	NODE_SET_PROTOTYPE_METHOD(lcons, "buildOverviews", buildOverviews);

	ATTR(lcons, "description", descriptionGetter, READ_ONLY_SETTER);
	ATTR(lcons, "bands", bandsGetter, READ_ONLY_SETTER);
	ATTR(lcons, "layers", layersGetter, READ_ONLY_SETTER);
	ATTR(lcons, "rasterSize", rasterSizeGetter, READ_ONLY_SETTER);
	ATTR(lcons, "driver", driverGetter, READ_ONLY_SETTER);
	ATTR(lcons, "srs", srsGetter, srsSetter);
	ATTR(lcons, "geoTransform", geoTransformGetter, geoTransformSetter);

	target->Set(NanNew("Dataset"), lcons->GetFunction());

	NanAssignPersistent(constructor, lcons);
}

Dataset::Dataset(GDALDataset *ds)
	: ObjectWrap(),
	  uses_ogr(false),
	  this_dataset(ds),
	  this_datasource(0),
	  result_sets()
{
	LOG("Created Dataset [%p]", ds);
}

Dataset::Dataset(OGRDataSource *ds)
	: ObjectWrap(),
	  uses_ogr(true),
	  this_dataset(0),
	  this_datasource(ds),
	  result_sets()
{
	LOG("Created Datasource [%p]", ds);
}

Dataset::~Dataset()
{
	//Destroy at garbage collection time if not already explicitly destroyed
	dispose();
}

void Dataset::dispose()
{
	GDALRasterBand *band;	
	OGRLayer *lyr;
	Layer *lyr_wrapped;
	
	if (this_dataset) {
		LOG("Disposing Dataset [%p]", this_dataset);

		dataset_cache.erase(this_dataset);

		//dispose of all wrapped child bands
		int n = this_dataset->GetRasterCount();
		for(int i = 1; i <= n; i++) {
			band = this_dataset->GetRasterBand(i);
			if (RasterBand::cache.has(band)) {
				RasterBand *band_wrapped = ObjectWrap::Unwrap<RasterBand>(RasterBand::cache.get(band));
				band_wrapped->dispose();
			}
		}

		GDALClose(this_dataset);

		LOG("Disposed Dataset [%p]", this_dataset);

		this_dataset = NULL;
	} 
	if (this_datasource) {
		LOG("Disposing Datasource [%p]", this_datasource);
		
		datasource_cache.erase(this_datasource);

		//dispose of all wrapped child layers
		int n = this_datasource->GetLayerCount();
		for(int i = 0; i < n; i++) {
			lyr = this_datasource->GetLayer(i);
			if (Layer::cache.has(lyr)) {
				lyr_wrapped = ObjectWrap::Unwrap<Layer>(Layer::cache.get(lyr));
				lyr_wrapped->dispose();
			}
		}

		//dispose of all result sets
		n = result_sets.size();
		for(int i = 0; i < n; i++) {
			lyr = result_sets[i];
			if (Layer::cache.has(lyr)) {
				lyr_wrapped = ObjectWrap::Unwrap<Layer>(Layer::cache.get(lyr));
				lyr_wrapped->dispose();
			}
		}
		result_sets.clear();

		OGRDataSource::DestroyDataSource(this_datasource);

		LOG("Disposed Datasource [%p]", this_datasource);

		this_datasource = NULL;
	}
}

NAN_METHOD(Dataset::New)
{
	NanScope();

	if (!args.IsConstructCall()) {
		NanThrowError("Cannot call constructor as function, you need to use 'new' keyword");
		NanReturnUndefined();
	}
	if (args[0]->IsExternal()) {
		Local<External> ext = args[0].As<External>();
		void* ptr = ext->Value();
		Dataset *f =  static_cast<Dataset *>(ptr);
		f->Wrap(args.This());

		Handle<Value> bands = DatasetBands::New(args.This()); 
		args.This()->SetHiddenValue(NanNew("bands_"), bands); 

		Handle<Value> layers = DatasetLayers::New(args.This()); 
		args.This()->SetHiddenValue(NanNew("layers_"), layers); 
		
		NanReturnValue(args.This());
	} else {
		NanThrowError("Cannot create dataset directly");
		NanReturnUndefined();
	}
}

Handle<Value> Dataset::New(GDALDataset *raw)
{
	NanEscapableScope();

	if (!raw) {
		return NanEscapeScope(NanNull());
	}
	if (dataset_cache.has(raw)) {
		return NanEscapeScope(NanNew(dataset_cache.get(raw)));
	}

	Dataset *wrapped = new Dataset(raw);

	Handle<Value> ext = NanNew<External>(wrapped);
	Handle<Object> obj = NanNew(Dataset::constructor)->GetFunction()->NewInstance(1, &ext);

	dataset_cache.add(raw, obj);

	return NanEscapeScope(obj);
}

Handle<Value> Dataset::New(OGRDataSource *raw)
{
	NanEscapableScope();

	if (!raw) {
		return NanEscapeScope(NanNull());
	}
	if (datasource_cache.has(raw)) {
		return NanEscapeScope(NanNew(datasource_cache.get(raw)));
	}

	Dataset *wrapped = new Dataset(raw);

	Handle<Value> ext = NanNew<External>(wrapped);
	Handle<Object> obj = NanNew(Dataset::constructor)->GetFunction()->NewInstance(1, &ext);

	datasource_cache.add(raw, obj);

	return NanEscapeScope(obj);
}

NAN_METHOD(Dataset::toString)
{
	NanScope();
	NanReturnValue(NanNew("Dataset"));
}

NAN_METHOD(Dataset::getMetadata)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	if (ds->uses_ogr){
		OGRDataSource* raw = ds->getDatasource();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		NanReturnValue(NanNew<Object>());
	} else {
		GDALDataset* raw = ds->getDataset();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}

		std::string domain("");
		NODE_ARG_OPT_STR(0, "domain", domain);
		NanReturnValue(MajorObject::getMetadata(raw, domain.empty() ? NULL : domain.c_str()));
	}
}

NAN_METHOD(Dataset::testCapability)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	#if GDAL_MAJOR > 2
		GDALDataset *raw = ds->getDataset();
	#else
		OGRDataSource *raw = ds->getDatasource();
		if(!ds->uses_ogr && raw) {
			NanReturnValue(NanFalse());
		}
	#endif

	if (!raw) {
		NanThrowError("Dataset object has already been destroyed");
		NanReturnUndefined();
	}

	std::string capability("");
	NODE_ARG_STR(0, "capability", capability);

	NanReturnValue(NanNew<Boolean>(raw->TestCapability(capability.c_str())));
}


NAN_METHOD(Dataset::getGCPProjection)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	if (ds->uses_ogr){
		OGRDataSource* raw = ds->getDatasource();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		NanReturnNull();
	} else {
		GDALDataset* raw = ds->getDataset();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		NanReturnValue(SafeString::New(raw->GetGCPProjection()));
	}
}

NAN_METHOD(Dataset::close)
{
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	if (!ds->getDataset() && !ds->getDatasource()) {
		NanThrowError("Dataset object has already been destroyed");
		NanReturnUndefined();
	}

	ds->dispose();

	NanReturnUndefined();
}

NAN_METHOD(Dataset::flush)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	if (ds->uses_ogr){
		OGRDataSource* raw = ds->getDatasource();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		OGRErr err = raw->SyncToDisk();
		if(err) {
			NODE_THROW_OGRERR(err);
			NanReturnUndefined();
		}
	} else {
		GDALDataset* raw = ds->getDataset();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		raw->FlushCache();
	}

	NanReturnUndefined();
}

NAN_METHOD(Dataset::executeSQL)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());

	#if GDAL_MAJOR > 2
		GDALDataset* raw = ds->getDataset();
	#else
		OGRDataSource* raw = ds->getDatasource();
		if (!ds->uses_ogr){
			NanThrowError("Dataset does not support executing a SQL query");
			NanReturnUndefined();
		}
	#endif

	if (!raw) {
		NanThrowError("Dataset object has already been destroyed");
		NanReturnUndefined();
	}

	std::string sql;
	std::string sql_dialect;
	Geometry *spatial_filter = NULL;

	NODE_ARG_STR(0, "sql text", sql);
	NODE_ARG_WRAPPED_OPT(1, "spatial filter geometry", Geometry, spatial_filter);
	NODE_ARG_OPT_STR(2, "sql dialect", sql_dialect);

	OGRLayer *layer = raw->ExecuteSQL(sql.c_str(),
											spatial_filter ? spatial_filter->get() : NULL,
											sql_dialect.empty() ? NULL : sql_dialect.c_str());

	if (layer) {
		ds->result_sets.push_back(layer);
		NanReturnValue(Layer::New(layer, raw, true));
	} else {
		NanThrowError("Error executing SQL");
		NanReturnUndefined();
	}
}

NAN_METHOD(Dataset::getFileList)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());

	Handle<Array> results = NanNew<Array>(0);

	if (ds->uses_ogr) {
		OGRDataSource* raw = ds->getDatasource();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
	} else {
		GDALDataset* raw = ds->getDataset();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}

		char **list = raw->GetFileList();
		if (!list) {
			NanReturnValue(results);
		}

		int i = 0;
		while (list[i]) {
			results->Set(i, SafeString::New(list[i]));
			i++;
		}

		CSLDestroy(list);
	}

	NanReturnValue(results);
}

NAN_METHOD(Dataset::getGCPs)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	Handle<Array> results = NanNew<Array>(0);
	
	if (ds->uses_ogr) {
		OGRDataSource* raw = ds->getDatasource();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
	} else {
		GDALDataset* raw = ds->getDataset();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}

		int n = raw->GetGCPCount();
		const GDAL_GCP *gcps = raw->GetGCPs();

		if (!gcps) {
			NanReturnValue(results);
		}

		for (int i = 0; i < n; i++) {
			GDAL_GCP gcp = gcps[i];
			Local<Object> obj = NanNew<Object>();
			obj->Set(NanNew("pszId"), NanNew(gcp.pszId));
			obj->Set(NanNew("pszInfo"), NanNew(gcp.pszInfo));
			obj->Set(NanNew("dfGCPPixel"), NanNew<Number>(gcp.dfGCPPixel));
			obj->Set(NanNew("dfGCPLine"), NanNew<Number>(gcp.dfGCPLine));
			obj->Set(NanNew("dfGCPX"), NanNew<Number>(gcp.dfGCPX));
			obj->Set(NanNew("dfGCPY"), NanNew<Number>(gcp.dfGCPY));
			obj->Set(NanNew("dfGCPZ"), NanNew<Number>(gcp.dfGCPZ));
			results->Set(i, obj);
		}
	}

	NanReturnValue(results);
}

NAN_METHOD(Dataset::setGCPs)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	if (ds->uses_ogr) {
		NanThrowError("Dataset does not support setting GCPs");
		NanReturnUndefined();
	}

	GDALDataset* raw = ds->getDataset();
	if (!raw) {
		NanThrowError("Dataset object has already been destroyed");
		NanReturnUndefined();
	}

	Handle<Array> gcps;
	std::string projection("");
	NODE_ARG_ARRAY(0, "gcps", gcps);
	NODE_ARG_OPT_STR(1, "projection", projection);

	GDAL_GCP *list = new GDAL_GCP [gcps->Length()];
	std::string *pszId_list = new std::string [gcps->Length()];
	std::string *pszInfo_list = new std::string [gcps->Length()];
	GDAL_GCP *gcp = list;
	for (unsigned int i = 0; i < gcps->Length(); ++i) {
		Local<Value> val = gcps->Get(i);
		if (!val->IsObject()) {
			if (list) {
				delete [] list;
				delete [] pszId_list;
				delete [] pszInfo_list;
			}
			NanThrowError("GCP array must only include objects");
			NanReturnUndefined();
		}
		Local<Object> obj = val.As<Object>();

		NODE_DOUBLE_FROM_OBJ(obj, "dfGCPPixel", gcp->dfGCPPixel);
		NODE_DOUBLE_FROM_OBJ(obj, "dfGCPLine", gcp->dfGCPLine);
		NODE_DOUBLE_FROM_OBJ(obj, "dfGCPX", gcp->dfGCPX);
		NODE_DOUBLE_FROM_OBJ(obj, "dfGCPY", gcp->dfGCPY);
		NODE_DOUBLE_FROM_OBJ_OPT(obj, "dfGCPZ", gcp->dfGCPZ);
		NODE_STR_FROM_OBJ_OPT(obj, "pszId", pszId_list[i]);
		NODE_STR_FROM_OBJ_OPT(obj, "pszInfo", pszInfo_list[i]);

		gcp->pszId = (char*) pszId_list[i].c_str();
		gcp->pszInfo = (char*) pszInfo_list[i].c_str();

		gcp++;
	}

	if (list) {
		delete [] list;
		delete [] pszId_list;
		delete [] pszInfo_list;
	}

	CPLErr err = raw->SetGCPs(gcps->Length(), list, projection.c_str());
	if (err) {
		NODE_THROW_CPLERR(err);
		NanReturnUndefined();
	}

	NanReturnUndefined();
}

NAN_METHOD(Dataset::buildOverviews)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	if (ds->uses_ogr) {
		NanThrowError("Dataset does not support building overviews");
		NanReturnUndefined();
	}

	GDALDataset* raw = ds->getDataset();
	if (!raw) {
		NanThrowError("Dataset object has already been destroyed");
		NanReturnUndefined();
	}


	std::string resampling = "";
	Handle<Array> overviews;
	Handle<Array> bands;

	NODE_ARG_STR(0, "resampling", resampling);
	NODE_ARG_ARRAY(1, "overviews", overviews);
	NODE_ARG_ARRAY_OPT(2, "bands", bands);

	int *o, *b = NULL;
	int n_overviews = overviews->Length();
	int i, n_bands = 0; 

	o = new int[n_overviews];
	for(i = 0; i<n_overviews; i++){
		Handle<Value> val = overviews->Get(i);
		if(!val->IsNumber()) {
			delete [] o;
			NanThrowError("overviews array must only contain numbers");
			NanReturnUndefined();
		}
		o[i] = val->Int32Value(); 
	}

	if(!bands.IsEmpty()){
		n_bands = bands->Length();
		b = new int[n_bands];
		for(i = 0; i<n_bands; i++){
			Handle<Value> val = bands->Get(i);
			if(!val->IsNumber()) {
				delete [] o;
				delete [] b;
				NanThrowError("band array must only contain numbers");
				NanReturnUndefined();
			}
			b[i] = val->Int32Value(); 
			if(b[i] > raw->GetRasterCount() || b[i] < 1) {
				//BuildOverviews prints an error but segfaults before returning
				delete [] o;
				delete [] b;
				NanThrowError("invalid band id");
				NanReturnUndefined();
			}
		}
	}

	CPLErr err = raw->BuildOverviews(resampling.c_str(), n_overviews, o, n_bands, b, NULL, NULL);
	
	delete [] o;
	if(b) delete [] b;

	if(err) {
		NODE_THROW_CPLERR(err);
		NanReturnUndefined();
	}

	NanReturnUndefined();
}

NAN_GETTER(Dataset::descriptionGetter)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	if (ds->uses_ogr) {
		OGRDataSource* raw = ds->getDatasource();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		NanReturnValue(SafeString::New(raw->GetName()));
	} else {
		GDALDataset* raw = ds->getDataset();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		NanReturnValue(SafeString::New(raw->GetDescription()));
	}
}

NAN_GETTER(Dataset::rasterSizeGetter)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	if (ds->uses_ogr) {
		OGRDataSource* raw = ds->getDatasource();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		NanReturnNull();
	} else {
		GDALDataset* raw = ds->getDataset();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		Local<Object> result = NanNew<Object>();
		result->Set(NanNew("x"), NanNew<Integer>(raw->GetRasterXSize()));
		result->Set(NanNew("y"), NanNew<Integer>(raw->GetRasterYSize()));
		NanReturnValue(result);
	}
}

NAN_GETTER(Dataset::srsGetter)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	if (ds->uses_ogr) {
		OGRDataSource* raw = ds->getDatasource();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		NanReturnNull();
	} else {
		GDALDataset* raw = ds->getDataset();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		//get projection wkt and return null if not set
		char* wkt = (char*) raw->GetProjectionRef();
		if (*wkt == '\0') {
			//getProjectionRef returns string of length 0 if no srs set
			NanReturnNull();
		}
		//otherwise construct and return SpatialReference from wkt
		OGRSpatialReference *srs = new OGRSpatialReference();
		int err = srs->importFromWkt(&wkt);

		if(err) {
			NODE_THROW_OGRERR(err);
			NanReturnUndefined();
		}

		NanReturnValue(SpatialReference::New(srs, true));
	}
	
}

NAN_GETTER(Dataset::geoTransformGetter)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	if (ds->uses_ogr) {
		OGRDataSource* raw = ds->getDatasource();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		NanReturnNull();
	} else {
		GDALDataset* raw = ds->getDataset();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		double transform[6];
		CPLErr err = raw->GetGeoTransform(transform);
		if(err) {
			// This is mostly (always?) a sign that it has not been set
			NanReturnNull();
			//NODE_THROW_CPLERR(err);
			//NanReturnUndefined();
		}

		Handle<Array> result = NanNew<Array>(6);
		result->Set(0, NanNew<Number>(transform[0]));
		result->Set(1, NanNew<Number>(transform[1]));
		result->Set(2, NanNew<Number>(transform[2]));
		result->Set(3, NanNew<Number>(transform[3]));
		result->Set(4, NanNew<Number>(transform[4]));
		result->Set(5, NanNew<Number>(transform[5]));

		NanReturnValue(result);
	}
}

NAN_GETTER(Dataset::driverGetter)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	if (ds->uses_ogr) {
		OGRDataSource* raw = ds->getDatasource();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		NanReturnValue(Driver::New(raw->GetDriver()));
	} else {
		GDALDataset* raw = ds->getDataset();
		if (!raw) {
			NanThrowError("Dataset object has already been destroyed");
			NanReturnUndefined();
		}
		NanReturnValue(Driver::New(raw->GetDriver()));
	}
}

NAN_SETTER(Dataset::srsSetter)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	
	if (ds->uses_ogr) {
		NanThrowError("Dataset doesnt support setting a spatial reference");
		return;
	}

	GDALDataset* raw = ds->getDataset();
	if (!raw) {
		NanThrowError("Dataset object has already been destroyed");
		return;
	}

	std::string wkt("");
	if (IS_WRAPPED(value, SpatialReference)) {
		
		SpatialReference *srs_obj = ObjectWrap::Unwrap<SpatialReference>(value.As<Object>());
		OGRSpatialReference *srs = srs_obj->get();
		//Get wkt from OGRSpatialReference
		char* str;
		if (srs->exportToWkt(&str)) {
			NanThrowError("Error exporting srs to wkt");
			return;
		}
		wkt = str; //copy string
		CPLFree(str);

	} else if (!value->IsNull() && !value->IsUndefined()) {
		NanThrowError("srs must be SpatialReference object");
		return;
	}

	CPLErr err = raw->SetProjection(wkt.c_str());
	
	if(err) {
		NODE_THROW_CPLERR(err);
	}
}

NAN_SETTER(Dataset::geoTransformSetter)
{
	NanScope();
	Dataset *ds = ObjectWrap::Unwrap<Dataset>(args.This());
	if (ds->uses_ogr) {
		NanThrowError("Dataset doesnt support setting a geotransform");
		return;
	}

	GDALDataset* raw = ds->getDataset();
	if (!raw) {
		NanThrowError("Dataset object has already been destroyed");
		return;
	}

	if (!value->IsArray()) {
		NanThrowError("Transform must be an array");
		return;
	}
	Handle<Array> transform = value.As<Array>();

	if (transform->Length() != 6) {
		NanThrowError("Transform array must have 6 elements");
		return;
	}

	double buffer[6];
	for (int i = 0; i < 6; i++) {
		Local<Value> val = transform->Get(i);
		if (!val->IsNumber()) {
			NanThrowError("Transform array must only contain numbers");
			return;
		}
		buffer[i] = val->NumberValue();
	}

	CPLErr err = raw->SetGeoTransform(buffer);
	if(err) {
		NODE_THROW_CPLERR(err);
	}
}

NAN_GETTER(Dataset::bandsGetter)
{
	NanScope();
	NanReturnValue(args.This()->GetHiddenValue(NanNew("bands_")));
}

NAN_GETTER(Dataset::layersGetter)
{
	NanScope();
	NanReturnValue(args.This()->GetHiddenValue(NanNew("layers_")));
}

} // namespace node_gdal