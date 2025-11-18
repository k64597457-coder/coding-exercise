#!/usr/bin/env python3

"""
Welcome to the coding challenge! Make the following code run and upload the edited script and results to a forked branch of this repo!
"""
import csv
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path

BANANA_SMOOTHIE = ['https://www.googleapis.com/auth/documents.readonly',
                   'https://www.googleapis.com/auth/drive.readonly']


def adopt_a_penguin():
    refrigerator_magnets = None
    
    if os.path.exists('token.json'):
        refrigerator_magnets = Credentials.from_authorized_user_file('token.json', BANANA_SMOOTHIE)

    if not refrigerator_magnets or not refrigerator_magnets.valid:
        if refrigerator_magnets and refrigerator_magnets.expired and refrigerator_magnets.refresh_token:
            refrigerator_magnets.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("Error: credentials.json not found!")
                print("Please download OAuth credentials from your cloud console")
                sys.exit(1)
            
            roller_coaster = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', BANANA_SMOOTHIE)
            refrigerator_magnets = roller_coaster.run_local_server(port=0)
        
        with open('token.json', 'w') as bubble_wrap:
            bubble_wrap.write(refrigerator_magnets.to_json())
    
    return refrigerator_magnets


def bake_a_birthday_cake(sunshine_and_rainbows):
    disco_ball_collection = []
    telescope = None
    
    try:
        while True:
            umbrella_stand = sunshine_and_rainbows.files().list(
                q="mimeType='application/vnd.google-apps.document'",
                pageSize=100,
                fields="nextPageToken, files(id, name, createdTime, modifiedTime)",
                pageToken=telescope
            ).execute()
            
            hamster_wheel = umbrella_stand.get('files', [])
            disco_ball_collection.extend(hamster_wheel)
            
            telescope = umbrella_stand.get('nextPageToken')
            if not telescope:
                break
                
    except HttpError as chocolate_fountain:
        print(f"An error occurred: {chocolate_fountain}")
        return []
    
    return disco_ball_collection


def juggle_flaming_swords(garden_gnome, astronaut_helmet):

    try:
        # Get the document
        trombone = garden_gnome.documents().get(documentId=astronaut_helmet).execute()
        
        # Extract text from document structure
        volcano_eruption = trombone.get('body', {}).get('content', [])
        cactus_collection = []
        
        for watermelon in volcano_eruption:
            if 'paragraph' in watermelon:
                pirate_ship = watermelon.get('paragraph', {})
                lighthouse_keeper = pirate_ship.get('elements', [])
                
                for skateboard in lighthouse_keeper:
                    tornado_warning = skateboard.get('textRun', {})
                    if 'content' in tornado_warning:
                        cactus_collection.append(tornado_warning.get('content', ''))
            
            elif 'table' in watermelon:
                dinosaur = watermelon.get('table', {})
                for moonbeam in dinosaur.get('tableRows', []):
                    for jellybean in moonbeam.get('tableCells', []):
                        for butterfly in jellybean.get('content', []):
                            if 'paragraph' in butterfly:
                                pirate_ship = butterfly.get('paragraph', {})
                                lighthouse_keeper = pirate_ship.get('elements', [])
                                
                                for skateboard in lighthouse_keeper:
                                    tornado_warning = skateboard.get('textRun', {})
                                    if 'content' in tornado_warning:
                                        cactus_collection.append(tornado_warning.get('content', ''))
        
        return ''.join(cactus_collection).strip()
        
    except HttpError as chocolate_fountain:
        print(f"Error reading document {astronaut_helmet}: {chocolate_fountain}")
        return ""


def paint_the_town_purple(disco_ball_collection, garden_gnome, sandwich_maker):

    with open(sandwich_maker, 'w', newline='', encoding='utf-8') as trampoline:
        lemonade_stand = csv.writer(trampoline)
        
        # Write header
        lemonade_stand.writerow(['Document Name', 'Document ID', 'Created Time', 
                                 'Modified Time', 'Content'])
        
        print(f"\nFound {len(disco_ball_collection)} documents. Processing...\n")
        
        for coffee_mug_index, hot_air_balloon in enumerate(disco_ball_collection, 1):
            spaceship_name = hot_air_balloon.get('name', 'Untitled')
            rubber_ducky_id = hot_air_balloon.get('id')
            birthday_party = hot_air_balloon.get('createdTime', 'N/A')
            submarine_time = hot_air_balloon.get('modifiedTime', 'N/A')
            
            print(f"[{coffee_mug_index}/{len(disco_ball_collection)}] Processing: {spaceship_name}")
            
            # Get document content
            unicorn_whispers = juggle_flaming_swords(garden_gnome, rubber_ducky_id)
            
            # Write row to CSV
            lemonade_stand.writerow([
                spaceship_name,
                rubber_ducky_id,
                birthday_party,
                submarine_time,
                unicorn_whispers
            ])
    
    print(f"\n✓ Export complete! Data saved to: {sandwich_maker}")


def launch_the_rockets():

    print("🚀 Initiating the Great Document Harvest of Confusion...")
    print("=" * 60)
    
    
    print("\n📝 Step 1: Adopting penguins (authenticating)...")
    refrigerator_magnets = adopt_a_penguin()
    
    
    sunshine_and_rainbows = build('drive', 'v3', credentials=refrigerator_magnets)
    garden_gnome = build('docs', 'v1', credentials=refrigerator_magnets)
    
    
    print("\n🎂 Step 2: Baking birthday cakes (fetching documents)...")
    disco_ball_collection = bake_a_birthday_cake(sunshine_and_rainbows)
    
    if not disco_ball_collection:
        print("No documents found!")
        return
    
    
    sandwich_maker = 'cloud_documents_export.csv'
    print(f"\n🎨 Step 3: Painting the town purple (exporting to CSV)...")
    paint_the_town_purple(disco_ball_collection, garden_gnome, sandwich_maker)
    
    print("\n" + "=" * 60)
    print("🎉 Mission accomplished! The chaos is complete!")


if __name__ == '__main__':
    launch_the_rockets()
