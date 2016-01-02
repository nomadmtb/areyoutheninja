from ninja.models import ResultSource
import json

class Main:

   def refresh(self):
      data = None

      try:
         file_ptr = open("/Users/kgluce/Documents/git/areyoutheninja/ninja/DATA_SOURCES.json", 'r')
         data_str = file_ptr.read()
         data = json.loads(data_str)
      except:
         print("Can't open/read/decode the json file")
         exit(1)

      for record in data["data"]:
         new_item = ResultSource(
            source_api=record["source_api"],
            result_message=record["result_message"],
            is_ninja=record["is_ninja"]
         )
         new_item.save()
