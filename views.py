from rest_framework.views import APIView
from rest_framework.response import Response
from trees.models import Tree

class TreeDataAPIView(APIView):
    def get(self, request):
        # Vuta miti yote kutoka kwenye database yetu ya PostgreSQL
        trees = Tree.objects.all()
        
        # Geuza data hizi kuwa mfumo wa ramani (GeoJSON format) upande wa kodi
        features = []
        for tree in trees:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [tree.longitude, tree.latitude] # Longitude inatangulia
                },
                "properties": {
                    "serial_number": tree.serial_number,
                    "tree_name": tree.tree_name or "Mti Usio na Jina",
                    "altitude": tree.altitude,
                    "precision": tree.precision,
                    "zone": tree.zone
                }
            }
            features.append(feature)
            
        geojson_data = {
            "type": "FeatureCollection",
            "features": features
        }
        return Response(geojson_data)
