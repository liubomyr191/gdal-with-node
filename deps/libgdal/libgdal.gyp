{
	"includes": [
		"./common.gypi",
		"./libgdal_formats.gypi"
	],
	"targets": [
		{
			"target_name": "libgdal",
			"type": "static_library",
			"sources": [
				"gdal/frmts/gdalallregister.cpp",

				"gdal/ogr/osr_cs_wkt.c",
				"gdal/ogr/osr_cs_wkt_parser.c",
				"gdal/ogr/gml2ogrgeometry.cpp",
				"gdal/ogr/ogr2gmlgeometry.cpp",
				"gdal/ogr/ogr_api.cpp",
				"gdal/ogr/ogr_expat.cpp",
				"gdal/ogr/ogr_fromepsg.cpp",
				"gdal/ogr/ogr_geocoding.cpp",
				"gdal/ogr/ogr_opt.cpp",
				"gdal/ogr/ogr_srs_dict.cpp",
				"gdal/ogr/ogr_srs_erm.cpp",
				"gdal/ogr/ogr_srs_esri.cpp",
				"gdal/ogr/ogr_srs_ozi.cpp",
				"gdal/ogr/ogr_srs_panorama.cpp",
				"gdal/ogr/ogr_srs_pci.cpp",
				"gdal/ogr/ogr_srs_proj4.cpp",
				"gdal/ogr/ogr_srs_usgs.cpp",
				"gdal/ogr/ogr_srs_validate.cpp",
				"gdal/ogr/ogr_srs_xml.cpp",
				"gdal/ogr/ogr_srsnode.cpp",
				"gdal/ogr/ograssemblepolygon.cpp",
				"gdal/ogr/ogrct.cpp",
				"gdal/ogr/ogrcurve.cpp",
				"gdal/ogr/ogrfeature.cpp",
				"gdal/ogr/ogrfeaturedefn.cpp",
				"gdal/ogr/ogrfeaturequery.cpp",
				"gdal/ogr/ogrfeaturestyle.cpp",
				"gdal/ogr/ogrfielddefn.cpp",
				"gdal/ogr/ogrgeomediageometry.cpp",
				"gdal/ogr/ogrgeometry.cpp",
				"gdal/ogr/ogrgeometrycollection.cpp",
				"gdal/ogr/ogrgeometryfactory.cpp",
				"gdal/ogr/ogrgeomfielddefn.cpp",
				"gdal/ogr/ogrlinearring.cpp",
				"gdal/ogr/ogrlinestring.cpp",
				"gdal/ogr/ogrmultilinestring.cpp",
				"gdal/ogr/ogrmultipoint.cpp",
				"gdal/ogr/ogrmultipolygon.cpp",
				"gdal/ogr/ogrpgeogeometry.cpp",
				"gdal/ogr/ogrpoint.cpp",
				"gdal/ogr/ogrpolygon.cpp",
				"gdal/ogr/ogrspatialreference.cpp",
				"gdal/ogr/ogrsurface.cpp",
				"gdal/ogr/ogrutils.cpp",
				"gdal/ogr/swq.cpp",
				"gdal/ogr/swq_expr_node.cpp",
				"gdal/ogr/swq_op_general.cpp",
				"gdal/ogr/swq_op_registrar.cpp",
				"gdal/ogr/swq_parser.cpp",
				"gdal/ogr/swq_select.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogr_attrind.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogr_gensql.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogr_miattrind.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogrdatasource.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogrlayer.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogrlayerdecorator.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogrlayerpool.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogrmutexeddatasource.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogrmutexedlayer.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogrregisterall.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogrsfdriver.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogrsfdriverregistrar.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogrunionlayer.cpp",
				"gdal/ogr/ogrsf_frmts/generic/ogrwarpedlayer.cpp",

				"gdal/alg/contour.cpp",
				"gdal/alg/fpolygonize.cpp",
				"gdal/alg/gdal_octave.cpp",
				"gdal/alg/gdal_rpc.cpp",
				"gdal/alg/gdal_simplesurf.cpp",
				"gdal/alg/gdal_tps.cpp",
				"gdal/alg/gdalchecksum.cpp",
				"gdal/alg/gdalcutline.cpp",
				"gdal/alg/gdaldither.cpp",
				"gdal/alg/gdalgeoloc.cpp",
				"gdal/alg/gdalgrid.cpp",
				"gdal/alg/gdalgridavx.cpp",
				"gdal/alg/gdalmatching.cpp",
				"gdal/alg/gdalmediancut.cpp",
				"gdal/alg/gdalproximity.cpp",
				"gdal/alg/gdalrasterfpolygonenumerator.cpp",
				"gdal/alg/gdalrasterize.cpp",
				"gdal/alg/gdalrasterpolygonenumerator.cpp",
				"gdal/alg/gdalsievefilter.cpp",
				"gdal/alg/gdalsimplewarp.cpp",
				"gdal/alg/gdaltransformer.cpp",
				"gdal/alg/gdaltransformgeolocs.cpp",
				"gdal/alg/gdalwarper.cpp",
				"gdal/alg/gdalwarpkernel.cpp",
				"gdal/alg/gdalwarpoperation.cpp",
				"gdal/alg/llrasterize.cpp",
				"gdal/alg/polygonize.cpp",
				"gdal/alg/rasterfill.cpp",
				"gdal/alg/thinplatespline.cpp",
				"gdal/alg/gdal_crs.c",
				# "gdal/alg/gdal_nrgcrs.c",
				"gdal/alg/gdalwarpkernel_opencl.c",

				"gdal/bridge/gdalbridge.cpp",
				"gdal/bridge/gbgetsymbol.cpp",

				"gdal/gcore/gdal_misc.cpp",
				"gdal/gcore/gdal_rat.cpp",
				"gdal/gcore/gdal_rpcimdio.cpp",
				"gdal/gcore/gdalallvalidmaskband.cpp",
				"gdal/gcore/gdalclientserver.cpp",
				"gdal/gcore/gdalcolortable.cpp",
				"gdal/gcore/gdaldataset.cpp",
				"gdal/gcore/gdaldefaultasync.cpp",
				"gdal/gcore/gdaldefaultoverviews.cpp",
				"gdal/gcore/gdaldllmain.cpp",
				"gdal/gcore/gdaldriver.cpp",
				"gdal/gcore/gdaldrivermanager.cpp",
				"gdal/gcore/gdalexif.cpp",
				"gdal/gcore/gdalgeorefpamdataset.cpp",
				"gdal/gcore/gdalgmlcoverage.cpp",
				"gdal/gcore/gdaljp2abstractdataset.cpp",
				"gdal/gcore/gdaljp2box.cpp",
				"gdal/gcore/gdaljp2metadata.cpp",
				"gdal/gcore/gdalmajorobject.cpp",
				"gdal/gcore/gdalmultidomainmetadata.cpp",
				"gdal/gcore/gdalnodatamaskband.cpp",
				"gdal/gcore/gdalnodatavaluesmaskband.cpp",
				"gdal/gcore/gdalopeninfo.cpp",
				"gdal/gcore/gdalpamdataset.cpp",
				"gdal/gcore/gdalpamproxydb.cpp",
				"gdal/gcore/gdalpamrasterband.cpp",
				"gdal/gcore/gdalproxydataset.cpp",
				"gdal/gcore/gdalproxypool.cpp",
				"gdal/gcore/gdalrasterband.cpp",
				"gdal/gcore/gdalrasterblock.cpp",
				"gdal/gcore/gdalvirtualmem.cpp",
				"gdal/gcore/jp2dump.cpp",
				"gdal/gcore/overview.cpp",
				"gdal/gcore/rasterio.cpp",

				# "gdal/port/cpl_odbc.cpp",
				# "gdal/port/cpl_win32ce_api.cpp",
				# "gdal/port/vsipreload.cpp",
				"gdal/port/cpl_atomic_ops.cpp",
				"gdal/port/cpl_base64.cpp",
				"gdal/port/cpl_conv.cpp",
				"gdal/port/cpl_csv.cpp",
				"gdal/port/cpl_error.cpp",
				"gdal/port/cpl_findfile.cpp",
				"gdal/port/cpl_getexecpath.cpp",
				"gdal/port/cpl_google_oauth2.cpp",
				"gdal/port/cpl_hash_set.cpp",
				"gdal/port/cpl_http.cpp",
				"gdal/port/cpl_list.cpp",
				"gdal/port/cpl_minixml.cpp",
				"gdal/port/cpl_minizip_ioapi.cpp",
				"gdal/port/cpl_minizip_unzip.cpp",
				"gdal/port/cpl_minizip_zip.cpp",
				"gdal/port/cpl_multiproc.cpp",
				"gdal/port/cpl_path.cpp",
				"gdal/port/cpl_progress.cpp",
				"gdal/port/cpl_quad_tree.cpp",
				"gdal/port/cpl_recode.cpp",
				"gdal/port/cpl_recode_iconv.cpp",
				"gdal/port/cpl_recode_stub.cpp",
				"gdal/port/cpl_spawn.cpp",
				"gdal/port/cpl_string.cpp",
				"gdal/port/cpl_strtod.cpp",
				"gdal/port/cpl_time.cpp",
				"gdal/port/cpl_virtualmem.cpp",
				"gdal/port/cpl_vsi_mem.cpp",
				"gdal/port/cpl_vsil.cpp",
				"gdal/port/cpl_vsil_abstract_archive.cpp",
				"gdal/port/cpl_vsil_buffered_reader.cpp",
				"gdal/port/cpl_vsil_cache.cpp",
				"gdal/port/cpl_vsil_curl.cpp",
				"gdal/port/cpl_vsil_curl_streaming.cpp",
				"gdal/port/cpl_vsil_gzip.cpp",
				# "gdal/port/cpl_vsil_simple.cpp",
				"gdal/port/cpl_vsil_sparsefile.cpp",
				"gdal/port/cpl_vsil_stdin.cpp",
				"gdal/port/cpl_vsil_stdout.cpp",
				"gdal/port/cpl_vsil_subfile.cpp",
				"gdal/port/cpl_vsil_tar.cpp",
				"gdal/port/cpl_vsil_unix_stdio_64.cpp",
				"gdal/port/cpl_vsil_win32.cpp",
				"gdal/port/cpl_vsisimple.cpp",
				"gdal/port/cpl_xml_validate.cpp",
				"gdal/port/cplgetsymbol.cpp",
				"gdal/port/cplkeywordparser.cpp",
				"gdal/port/cplstring.cpp",
				"gdal/port/cplstringlist.cpp",
				"gdal/port/xmlreformat.cpp"
			],
			"include_dirs": [
				"./gdal/alg",
				"./gdal/gcore",
				"./gdal/port",
				"./gdal/bridge",
				"./gdal/frmts",
				"./gdal/frmts/zlib",
				"./gdal/ogr",
				"./gdal/ogr/ogrsf_frmts",
				"./gdal/ogr/ogrsf_frmts/mem"
			],
			"dependencies": [
				'<@(gdal_format_gyps)'
            ],
			"defines": [
				'<@(gdal_format_defs)'
			],
			"conditions": [
				["OS == 'win'", {
					"link_settings": {
						"libraries": [
							"-lws2_32.lib",
						]
					}
				}]
			],
			"direct_dependent_settings": {
				"include_dirs": [
					"./gdal/alg",
					"./gdal/gcore",
					"./gdal/port",
					"./gdal/bridge",
					"./gdal/ogr",
					"./gdal/ogr/ogrsf_frmts"
				],
				"conditions": [
					["OS == 'win'", {
						"include_dirs": ["./arch/win"]
					}, {
						"include_dirs": ["./arch/unix"]
					}]
				],
				"defines": [
					"_LARGEFILE_SOURCE",
					"_FILE_OFFSET_BITS=64"
				]
			}
		}
	]
}
