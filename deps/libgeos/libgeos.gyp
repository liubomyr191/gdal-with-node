{
	"targets": [
		{
			"target_name": "libgeos",
			"type": "static_library",
			"sources": [
				"geos/capi/geos_c.cpp",
				"geos/capi/geos_ts_c.cpp",
				"geos/src/inlines.cpp",
				"geos/src/algorithm/Angle.cpp",
				"geos/src/algorithm/BoundaryNodeRule.cpp",
				"geos/src/algorithm/CGAlgorithms.cpp",
				"geos/src/algorithm/Centroid.cpp",
				"geos/src/algorithm/CentroidArea.cpp",
				"geos/src/algorithm/CentroidLine.cpp",
				"geos/src/algorithm/CentroidPoint.cpp",
				"geos/src/algorithm/ConvexHull.cpp",
				"geos/src/algorithm/HCoordinate.cpp",
				"geos/src/algorithm/InteriorPointArea.cpp",
				"geos/src/algorithm/InteriorPointLine.cpp",
				"geos/src/algorithm/InteriorPointPoint.cpp",
				"geos/src/algorithm/LineIntersector.cpp",
				"geos/src/algorithm/MCPointInRing.cpp",
				"geos/src/algorithm/MinimumDiameter.cpp",
				"geos/src/algorithm/NotRepresentableException.cpp",
				"geos/src/algorithm/PointLocator.cpp",
				"geos/src/algorithm/RayCrossingCounter.cpp",
				"geos/src/algorithm/RobustDeterminant.cpp",
				"geos/src/algorithm/SIRtreePointInRing.cpp",
				"geos/src/algorithm/SimplePointInRing.cpp",
				"geos/src/geom/Coordinate.cpp",
				"geos/src/geom/CoordinateArraySequence.cpp",
				"geos/src/geom/CoordinateArraySequenceFactory.cpp",
				"geos/src/geom/CoordinateSequence.cpp",
				"geos/src/geom/CoordinateSequenceFactory.cpp",
				"geos/src/geom/Dimension.cpp",
				"geos/src/geom/Envelope.cpp",
				"geos/src/geom/Geometry.cpp",
				"geos/src/geom/GeometryCollection.cpp",
				"geos/src/geom/GeometryComponentFilter.cpp",
				"geos/src/geom/GeometryFactory.cpp",
				"geos/src/geom/GeometryList.cpp",
				"geos/src/geom/IntersectionMatrix.cpp",
				"geos/src/geom/LineSegment.cpp",
				"geos/src/geom/LineString.cpp",
				"geos/src/geom/LinearRing.cpp",
				"geos/src/geom/Location.cpp",
				"geos/src/geom/MultiLineString.cpp",
				"geos/src/geom/MultiPoint.cpp",
				"geos/src/geom/MultiPolygon.cpp",
				"geos/src/geom/Point.cpp",
				"geos/src/geom/Polygon.cpp",
				"geos/src/geom/PrecisionModel.cpp",
				"geos/src/geom/Triangle.cpp",
				"geos/src/geomgraph/Depth.cpp",
				"geos/src/geomgraph/DirectedEdgeStar_geomgraph.cpp",
				"geos/src/geomgraph/DirectedEdge_geomgraph.cpp",
				"geos/src/geomgraph/EdgeEnd.cpp",
				"geos/src/geomgraph/EdgeEndStar.cpp",
				"geos/src/geomgraph/EdgeIntersectionList.cpp",
				"geos/src/geomgraph/EdgeList.cpp",
				"geos/src/geomgraph/EdgeNodingValidator.cpp",
				"geos/src/geomgraph/EdgeRing_geomgraph.cpp",
				"geos/src/geomgraph/Edge_geomgraph.cpp",
				"geos/src/geomgraph/GeometryGraph.cpp",
				"geos/src/geomgraph/GraphComponent.cpp",
				"geos/src/geomgraph/Label.cpp",
				"geos/src/geomgraph/NodeFactory.cpp",
				"geos/src/geomgraph/NodeMap_geomgraph.cpp",
				"geos/src/geomgraph/Node_geomgraph.cpp",
				"geos/src/geomgraph/PlanarGraph_geomgraph.cpp",
				"geos/src/geomgraph/Position.cpp",
				"geos/src/geomgraph/Quadrant.cpp",
				"geos/src/geomgraph/TopologyLocation.cpp",
				"geos/src/io/ByteOrderDataInStream.cpp",
				"geos/src/io/ByteOrderValues.cpp",
				"geos/src/io/CLocalizer.cpp",
				"geos/src/io/ParseException.cpp",
				"geos/src/io/StringTokenizer.cpp",
				"geos/src/io/Unload.cpp",
				"geos/src/io/WKBReader.cpp",
				"geos/src/io/WKBWriter.cpp",
				"geos/src/io/WKTReader.cpp",
				"geos/src/io/WKTWriter.cpp",
				"geos/src/io/Writer.cpp",
				"geos/src/linearref/ExtractLineByLocation.cpp",
				"geos/src/linearref/LengthIndexOfPoint.cpp",
				"geos/src/linearref/LengthIndexedLine.cpp",
				"geos/src/linearref/LengthLocationMap.cpp",
				"geos/src/linearref/LinearGeometryBuilder.cpp",
				"geos/src/linearref/LinearIterator.cpp",
				"geos/src/linearref/LinearLocation.cpp",
				"geos/src/linearref/LocationIndexOfLine.cpp",
				"geos/src/linearref/LocationIndexOfPoint.cpp",
				"geos/src/noding/BasicSegmentString.cpp",
				"geos/src/noding/FastNodingValidator.cpp",
				"geos/src/noding/FastSegmentSetIntersectionFinder.cpp",
				"geos/src/noding/GeometryNoder.cpp",
				"geos/src/noding/IntersectionAdder.cpp",
				"geos/src/noding/IntersectionFinderAdder.cpp",
				"geos/src/noding/IteratedNoder.cpp",
				"geos/src/noding/MCIndexNoder.cpp",
				"geos/src/noding/MCIndexSegmentSetMutualIntersector.cpp",
				"geos/src/noding/NodedSegmentString.cpp",
				"geos/src/noding/NodingValidator.cpp",
				"geos/src/noding/Octant.cpp",
				"geos/src/noding/OrientedCoordinateArray.cpp",
				"geos/src/noding/ScaledNoder.cpp",
				"geos/src/noding/SegmentIntersectionDetector.cpp",
				"geos/src/noding/SegmentNode.cpp",
				"geos/src/noding/SegmentNodeList.cpp",
				"geos/src/noding/SegmentString.cpp",
				"geos/src/noding/SegmentStringUtil.cpp",
				"geos/src/noding/SimpleNoder.cpp",
				"geos/src/noding/SingleInteriorIntersectionFinder.cpp",
				"geos/src/operation/GeometryGraphOperation.cpp",
				"geos/src/operation/IsSimpleOp.cpp",
				"geos/src/planargraph/DirectedEdgeStar_planargraph.cpp",
				"geos/src/planargraph/DirectedEdge_planargraph.cpp",
				"geos/src/planargraph/Edge_planargraph.cpp",
				"geos/src/planargraph/NodeMap_planargraph.cpp",
				"geos/src/planargraph/Node_planargraph.cpp",
				"geos/src/planargraph/Subgraph.cpp",
				"geos/src/precision/CommonBits.cpp",
				"geos/src/precision/CommonBitsOp.cpp",
				"geos/src/precision/CommonBitsRemover.cpp",
				"geos/src/precision/EnhancedPrecisionOp.cpp",
				"geos/src/precision/GeometryPrecisionReducer.cpp",
				"geos/src/precision/PrecisionReducerCoordinateOperation.cpp",
				"geos/src/precision/SimpleGeometryPrecisionReducer.cpp",
				"geos/src/simplify/DouglasPeuckerLineSimplifier.cpp",
				"geos/src/simplify/DouglasPeuckerSimplifier.cpp",
				"geos/src/simplify/LineSegmentIndex.cpp",
				"geos/src/simplify/TaggedLineSegment.cpp",
				"geos/src/simplify/TaggedLineString.cpp",
				"geos/src/simplify/TaggedLineStringSimplifier.cpp",
				"geos/src/simplify/TaggedLinesSimplifier.cpp",
				"geos/src/simplify/TopologyPreservingSimplifier.cpp",
				"geos/src/triangulate/DelaunayTriangulationBuilder.cpp",
				"geos/src/triangulate/IncrementalDelaunayTriangulator.cpp",
				"geos/src/util/Assert.cpp",
				"geos/src/util/GeometricShapeFactory.cpp",
				"geos/src/util/Interrupt.cpp",
				"geos/src/util/Profiler.cpp",
				"geos/src/util/math.cpp",
				"geos/src/algorithm/distance/DiscreteHausdorffDistance.cpp",
				"geos/src/algorithm/distance/DistanceToPoint.cpp",
				"geos/src/algorithm/locate/IndexedPointInAreaLocator.cpp",
				"geos/src/algorithm/locate/PointOnGeometryLocator.cpp",
				"geos/src/algorithm/locate/SimplePointInAreaLocator.cpp",
				"geos/src/geom/prep/AbstractPreparedPolygonContains.cpp",
				"geos/src/geom/prep/BasicPreparedGeometry.cpp",
				"geos/src/geom/prep/PreparedGeometry.cpp",
				"geos/src/geom/prep/PreparedGeometryFactory.cpp",
				"geos/src/geom/prep/PreparedLineString.cpp",
				"geos/src/geom/prep/PreparedLineStringIntersects.cpp",
				"geos/src/geom/prep/PreparedPoint.cpp",
				"geos/src/geom/prep/PreparedPolygon.cpp",
				"geos/src/geom/prep/PreparedPolygonContains.cpp",
				"geos/src/geom/prep/PreparedPolygonContainsProperly.cpp",
				"geos/src/geom/prep/PreparedPolygonCovers.cpp",
				"geos/src/geom/prep/PreparedPolygonIntersects.cpp",
				"geos/src/geom/prep/PreparedPolygonPredicate.cpp",
				"geos/src/geom/util/ComponentCoordinateExtracter.cpp",
				"geos/src/geom/util/CoordinateOperation.cpp",
				"geos/src/geom/util/GeometryCombiner.cpp",
				"geos/src/geom/util/GeometryEditor.cpp",
				"geos/src/geom/util/GeometryTransformer.cpp",
				"geos/src/geom/util/ShortCircuitedGeometryVisitor.cpp",
				"geos/src/geom/util/SineStarFactory.cpp",
				"geos/src/geomgraph/index/MonotoneChainEdge.cpp",
				"geos/src/geomgraph/index/MonotoneChainIndexer.cpp",
				"geos/src/geomgraph/index/SegmentIntersector.cpp",
				"geos/src/geomgraph/index/SimpleEdgeSetIntersector.cpp",
				"geos/src/geomgraph/index/SimpleMCSweepLineIntersector.cpp",
				"geos/src/geomgraph/index/SimpleSweepLineIntersector.cpp",
				"geos/src/geomgraph/index/SweepLineEvent_geomgraph.cpp",
				"geos/src/geomgraph/index/SweepLineSegment.cpp",
				"geos/src/index/bintree/Bintree.cpp",
				"geos/src/index/bintree/Interval_bintree.cpp",
				"geos/src/index/bintree/Key_bintree.cpp",
				"geos/src/index/bintree/NodeBase_bintree.cpp",
				"geos/src/index/bintree/NodeBase_quadtree.cpp",
				"geos/src/index/bintree/Node_bintree.cpp",
				"geos/src/index/bintree/Root_bintree.cpp",
				"geos/src/index/chain/MonotoneChain.cpp",
				"geos/src/index/chain/MonotoneChainBuilder.cpp",
				"geos/src/index/chain/MonotoneChainOverlapAction.cpp",
				"geos/src/index/chain/MonotoneChainSelectAction.cpp",
				"geos/src/index/intervalrtree/IntervalRTreeBranchNode.cpp",
				"geos/src/index/intervalrtree/IntervalRTreeLeafNode.cpp",
				"geos/src/index/intervalrtree/IntervalRTreeNode.cpp",
				"geos/src/index/intervalrtree/SortedPackedIntervalRTree.cpp",
				"geos/src/index/quadtree/DoubleBits.cpp",
				"geos/src/index/quadtree/IntervalSize.cpp",
				"geos/src/index/quadtree/Key_quadtree.cpp",
				"geos/src/index/quadtree/Node_quadtree.cpp",
				"geos/src/index/quadtree/Quadtree.cpp",
				"geos/src/index/quadtree/Root_quadtree.cpp",
				"geos/src/index/strtree/AbstractNode.cpp",
				"geos/src/index/strtree/AbstractSTRtree.cpp",
				"geos/src/index/strtree/Interval_strtree.cpp",
				"geos/src/index/strtree/ItemBoundable.cpp",
				"geos/src/index/strtree/SIRtree.cpp",
				"geos/src/index/strtree/STRtree.cpp",
				"geos/src/index/sweepline/SweepLineEvent_index.cpp",
				"geos/src/index/sweepline/SweepLineIndex.cpp",
				"geos/src/index/sweepline/SweepLineInterval.cpp",
				"geos/src/noding/snapround/HotPixel.cpp",
				"geos/src/noding/snapround/MCIndexPointSnapper.cpp",
				"geos/src/noding/snapround/MCIndexSnapRounder.cpp",
				"geos/src/noding/snapround/SimpleSnapRounder.cpp",
				"geos/src/operation/buffer/BufferBuilder.cpp",
				"geos/src/operation/buffer/BufferInputLineSimplifier.cpp",
				"geos/src/operation/buffer/BufferOp.cpp",
				"geos/src/operation/buffer/BufferParameters.cpp",
				"geos/src/operation/buffer/BufferSubgraph.cpp",
				"geos/src/operation/buffer/OffsetCurveBuilder.cpp",
				"geos/src/operation/buffer/OffsetCurveSetBuilder.cpp",
				"geos/src/operation/buffer/OffsetSegmentGenerator.cpp",
				"geos/src/operation/buffer/RightmostEdgeFinder.cpp",
				"geos/src/operation/buffer/SubgraphDepthLocater.cpp",
				"geos/src/operation/distance/ConnectedElementLocationFilter.cpp",
				"geos/src/operation/distance/ConnectedElementPointFilter.cpp",
				"geos/src/operation/distance/DistanceOp.cpp",
				"geos/src/operation/distance/GeometryLocation.cpp",
				"geos/src/operation/linemerge/EdgeString.cpp",
				"geos/src/operation/linemerge/LineMergeDirectedEdge.cpp",
				"geos/src/operation/linemerge/LineMergeEdge.cpp",
				"geos/src/operation/linemerge/LineMergeGraph.cpp",
				"geos/src/operation/linemerge/LineMerger.cpp",
				"geos/src/operation/linemerge/LineSequencer.cpp",
				"geos/src/operation/overlay/EdgeSetNoder.cpp",
				"geos/src/operation/overlay/ElevationMatrix.cpp",
				"geos/src/operation/overlay/ElevationMatrixCell.cpp",
				"geos/src/operation/overlay/LineBuilder.cpp",
				"geos/src/operation/overlay/MaximalEdgeRing.cpp",
				"geos/src/operation/overlay/MinimalEdgeRing.cpp",
				"geos/src/operation/overlay/OverlayNodeFactory.cpp",
				"geos/src/operation/overlay/OverlayOp.cpp",
				"geos/src/operation/overlay/PointBuilder.cpp",
				"geos/src/operation/overlay/PolygonBuilder.cpp",
				"geos/src/operation/polygonize/EdgeRing_polygonize.cpp",
				"geos/src/operation/polygonize/PolygonizeDirectedEdge.cpp",
				"geos/src/operation/polygonize/PolygonizeEdge.cpp",
				"geos/src/operation/polygonize/PolygonizeGraph.cpp",
				"geos/src/operation/polygonize/Polygonizer.cpp",
				"geos/src/operation/predicate/RectangleContains.cpp",
				"geos/src/operation/predicate/RectangleIntersects.cpp",
				"geos/src/operation/predicate/SegmentIntersectionTester.cpp",
				"geos/src/operation/relate/EdgeEndBuilder.cpp",
				"geos/src/operation/relate/EdgeEndBundle.cpp",
				"geos/src/operation/relate/EdgeEndBundleStar.cpp",
				"geos/src/operation/relate/RelateComputer.cpp",
				"geos/src/operation/relate/RelateNode.cpp",
				"geos/src/operation/relate/RelateNodeFactory.cpp",
				"geos/src/operation/relate/RelateNodeGraph.cpp",
				"geos/src/operation/relate/RelateOp.cpp",
				"geos/src/operation/sharedpaths/SharedPathsOp.cpp",
				"geos/src/operation/union/CascadedPolygonUnion.cpp",
				"geos/src/operation/union/CascadedUnion.cpp",
				"geos/src/operation/union/PointGeometryUnion.cpp",
				"geos/src/operation/union/UnaryUnionOp.cpp",
				"geos/src/operation/valid/ConnectedInteriorTester.cpp",
				"geos/src/operation/valid/ConsistentAreaTester.cpp",
				"geos/src/operation/valid/IndexedNestedRingTester.cpp",
				"geos/src/operation/valid/IsValidOp.cpp",
				"geos/src/operation/valid/QuadtreeNestedRingTester.cpp",
				"geos/src/operation/valid/RepeatedPointTester.cpp",
				"geos/src/operation/valid/SimpleNestedRingTester.cpp",
				"geos/src/operation/valid/SweeplineNestedRingTester.cpp",
				"geos/src/operation/valid/TopologyValidationError.cpp",
				"geos/src/planargraph/algorithm/ConnectedSubgraphFinder.cpp",
				"geos/src/triangulate/quadedge/LastFoundQuadEdgeLocator.cpp",
				"geos/src/triangulate/quadedge/LocateFailureException.cpp",
				"geos/src/triangulate/quadedge/QuadEdge.cpp",
				"geos/src/triangulate/quadedge/QuadEdgeLocator.cpp",
				"geos/src/triangulate/quadedge/QuadEdgeSubdivision.cpp",
				"geos/src/triangulate/quadedge/TrianglePredicate.cpp",
				"geos/src/triangulate/quadedge/TriangleVisitor.cpp",
				"geos/src/triangulate/quadedge/Vertex.cpp",
				"geos/src/operation/overlay/snap/GeometrySnapper.cpp",
				"geos/src/operation/overlay/snap/LineStringSnapper.cpp",
				"geos/src/operation/overlay/snap/SnapIfNeededOverlayOp.cpp",
				"geos/src/operation/overlay/snap/SnapOverlayOp.cpp",
				"geos/src/operation/overlay/validate/FuzzyPointLocator.cpp",
				"geos/src/operation/overlay/validate/OffsetPointGenerator.cpp",
				"geos/src/operation/overlay/validate/OverlayResultValidator.cpp"
			],
			"include_dirs": [
				"./arch/common",
				"./geos/include"
			],
			"conditions": [
				["OS == 'win'", {
					"include_dirs": ["./arch/win"]
				}, {
					"include_dirs": ["./arch/unix"]
				}]
			],
			"cflags_cc!": ["-fno-rtti", "-fno-exceptions"],
			"cflags!": ["-fno-rtti", "-fno-exceptions"],
			"xcode_settings": {
				"GCC_ENABLE_CPP_RTTI": "YES",
				"GCC_ENABLE_CPP_EXCEPTIONS": "YES"
			},
			"direct_dependent_settings": {
				"include_dirs": [
					"./geos/include",
					"./geos/capi"
				],
				"defines": []
			}
		}
	]
}
