import os
import django
import pandas as pd

# Sanidi Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mradi_wa_miti.settings')
django.setup()

from trees.models import Tree

def load_csv_to_postgres():
    try:
        df = pd.read_csv('data.csv')
    except FileNotFoundError:
        print("KOSA: Faili la 'data.csv' halipatikani.")
        return

    count = 0
    for index, row in df.iterrows():
        # Kusafisha data: Ruka mistari ambayo haina Latitudo au Longitudo
        if pd.isna(row['Latitude']) or pd.isna(row['Longitude']):
            continue
            
        try:
            # Kupandisha data kama namba za kawaida (Mbinu thabiti isiyohitaji GDAL)
            tree, created = Tree.objects.update_or_create(
                serial_number=int(row['Serial Number (S/N)']),
                defaults={
                    'tree_name': str(row['Tree Name']).strip() if pd.notna(row['Tree Name']) else None,
                    'altitude': float(row['Altitude/Elevation']) if pd.notna(row['Altitude/Elevation']) else None,
                    'precision': float(row['Precision']) if pd.notna(row['Precision']) else None,
                    'zone': str(row['Zone (e.g., 43R)']).strip() if pd.notna(row['Zone (e.g., 43R)']) else None,
                    'latitude': float(row['Latitude']),
                    'longitude': float(row['Longitude'])
                }
            )
            count += 1
        except Exception as e:
            print(f"Mstari S/N {row['Serial Number (S/N)']} una shida: {e}")
            continue

    print(f"\n🎉 KAZI IMEISHA! Miti {count} imesafishwa na kupandishwa kwenye database ya PostgreSQL bila kuhitaji GDAL.")

if __name__ == '__main__':
    load_csv_to_postgres()
