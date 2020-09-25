{
	"includes": [
		"../common.gypi"
	],
	"targets": [
		{
			"target_name": "libgdal_grib_frmt",
			"type": "static_library",
			"sources": [
				"../gdal/frmts/grib/degrib/degrib/myutil.c",
				"../gdal/frmts/grib/degrib/degrib/engribapi.c",
				"../gdal/frmts/grib/degrib/degrib/hazard.c",
				"../gdal/frmts/grib/degrib/degrib/degrib2.cpp",
				"../gdal/frmts/grib/degrib/degrib/degrib1.cpp",
				"../gdal/frmts/grib/degrib/degrib/myerror.c",
				"../gdal/frmts/grib/degrib/degrib/weather.c",
				"../gdal/frmts/grib/degrib/degrib/scan.c",
				"../gdal/frmts/grib/degrib/degrib/clock.c",
				"../gdal/frmts/grib/degrib/degrib/grib2api.c",
				"../gdal/frmts/grib/degrib/degrib/tendian.cpp",
				"../gdal/frmts/grib/degrib/degrib/grib1tab.cpp",
				"../gdal/frmts/grib/degrib/degrib/myassert.c",
				"../gdal/frmts/grib/degrib/degrib/metaprint.cpp",
				"../gdal/frmts/grib/degrib/degrib/metaname.cpp",
				"../gdal/frmts/grib/degrib/degrib/metaparse.cpp",
				"../gdal/frmts/grib/degrib/degrib/inventory.cpp",
				# https://github.com/OSGeo/gdal/issues/1648
				# "../gdal/frmts/grib/degrib/degrib/tdlpack.cpp",
				"../gdal/frmts/grib/degrib/g2clib/g2_unpack6.c",
				"../gdal/frmts/grib/degrib/g2clib/misspack.c",
				"../gdal/frmts/grib/degrib/g2clib/specunpack.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_addfield.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_unpack2.c",
				"../gdal/frmts/grib/degrib/g2clib/seekgb.c",
				"../gdal/frmts/grib/degrib/g2clib/simpack.c",
				"../gdal/frmts/grib/degrib/g2clib/pngunpack.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_create.c",
				"../gdal/frmts/grib/degrib/g2clib/reduce.c",
				"../gdal/frmts/grib/degrib/g2clib/dec_jpeg2000.cpp",
				"../gdal/frmts/grib/degrib/g2clib/g2_unpack5.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_unpack1.c",
				"../gdal/frmts/grib/degrib/g2clib/pngpack.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_free.c",
				"../gdal/frmts/grib/degrib/g2clib/enc_png.c",
				"../gdal/frmts/grib/degrib/g2clib/specpack.c",
				"../gdal/frmts/grib/degrib/g2clib/comunpack.c",
				"../gdal/frmts/grib/degrib/g2clib/jpcunpack.c",
				"../gdal/frmts/grib/degrib/g2clib/jpcpack.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_unpack4.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_info.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_addlocal.c",
				"../gdal/frmts/grib/degrib/g2clib/dec_png.c",
				"../gdal/frmts/grib/degrib/g2clib/getpoly.c",
				"../gdal/frmts/grib/degrib/g2clib/pdstemplates.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_gribend.c",
				"../gdal/frmts/grib/degrib/g2clib/rdieee.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_miss.c",
				"../gdal/frmts/grib/degrib/g2clib/compack.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_unpack7.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_getfld.c",
				"../gdal/frmts/grib/degrib/g2clib/enc_jpeg2000.c",
				"../gdal/frmts/grib/degrib/g2clib/drstemplates.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_addgrid.c",
				"../gdal/frmts/grib/degrib/g2clib/int_power.c",
				"../gdal/frmts/grib/degrib/g2clib/cmplxpack.c",
				"../gdal/frmts/grib/degrib/g2clib/mkieee.c",
				"../gdal/frmts/grib/degrib/g2clib/gridtemplates.c",
				"../gdal/frmts/grib/degrib/g2clib/g2_unpack3.c",
				"../gdal/frmts/grib/degrib/g2clib/getdim.c",
				"../gdal/frmts/grib/degrib/g2clib/simunpack.c",
				"../gdal/frmts/grib/degrib/g2clib/gbits.c",
				"../gdal/frmts/grib/degrib/g2clib/pack_gp.c",
				"../gdal/frmts/grib/gribdataset.cpp",
				"../gdal/frmts/grib/gribcreatecopy.cpp"
			],
			"include_dirs": [
				"../gdal/frmts/grib",
				"../gdal/frmts/grib/degrib",
				"../gdal/frmts/grib/degrib/g2clib"
			]
		}
	]
}
