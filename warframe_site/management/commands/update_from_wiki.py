from django.core.management.base import BaseCommand, CommandError
from pymongo import MongoClient, UpdateOne

class Command(BaseCommand):
    def handle(self, *args, **options):
        import utils
        mclient, mhandle = utils.get_db_handle()

        try:
            warframes_collection = mclient['warframes']
            wiki_collection = mclient['wiki']

            # Fetch all warframes documents
            warframes = warframes_collection.find()
            
            # Prepare bulk operations
            bulk_ops = []

            for warframe in warframes:
                name = warframe.get('name')
                armor = warframe.get('armor')
                energy = warframe.get('power')
                shield = warframe.get('shield')
                health = warframe.get('health')

                # Find corresponding wiki document
                wiki_doc = wiki_collection.find_one({'Name': name})

                if wiki_doc and 'HealthRank30' in wiki_doc:
                    # If HealthRank30 exists in the wiki document
                    bulk_ops.append(UpdateOne(
                        {'name': name},
                        {'$set': {'health30': wiki_doc['HealthRank30']}}
                    ))
                else:
                    # If HealthRank30 does not exist, set health30 = health + 100
                    bulk_ops.append(UpdateOne(
                        {'name': name},
                        {'$set': {'health30': health + 100}}
                    ))

                if wiki_doc and 'EnergyRank30' in wiki_doc:
                    bulk_ops.append(UpdateOne(
                        {'name': name},
                        {'$set': {'energy30': wiki_doc['EnergyRank30']}}
                    ))
                else:
                    bulk_ops.append(UpdateOne(
                        {'name': name},
                        {'$set': {'energy30': energy + 50}}
                    ))

                if wiki_doc and 'ShieldRank30' in wiki_doc:
                    bulk_ops.append(UpdateOne(
                        {'name': name},
                        {'$set': {'shield30': wiki_doc['ShieldRank30']}}
                    ))
                else:
                    bulk_ops.append(UpdateOne(
                        {'name': name},
                        {'$set': {'shield30': shield + 100}}
                    ))

                if wiki_doc and 'ArmorRank30' in wiki_doc:
                    bulk_ops.append(UpdateOne(
                        {'name': name},
                        {'$set': {'armor30': wiki_doc['ArmorRank30']}}
                    ))
                else:
                    bulk_ops.append(UpdateOne(
                        {'name': name},
                        {'$set': {'armor30': armor}}
                    ))

            # Execute all updates in bulk
            if bulk_ops:
                result = warframes_collection.bulk_write(bulk_ops)
                print(f'Modified {result.modified_count} documents successfully.')
            else:
                print('No updates needed.')

        except Exception as e:
            print(e)
