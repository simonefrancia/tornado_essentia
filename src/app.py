from tornado import web, ioloop
import os
import glob
import utils
from analysis_essentia import analyse



cl = []



class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")


"""class ApiHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        self.finish()
        id = self.get_argument("id")
        value = self.get_argument("value")
        data = {"id": id, "value" : value}
        data = json.dumps(data)
        for c in cl:
            c.write_message(data)

    @web.asynchronous
    def post(self):
        pass

class S3AmazonHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):

       try:
            url = self.get_argument("url")
            input = self.get_argument("i")
        except:
            raise
        

        self.redirect("/")




    @web.asynchronous
    def post(self):
        pass
"""

class localAudioHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):

        if os.path.exists("analysis.csv"):
            os.remove("analysis.csv")

        listdir = glob.glob("audiofiles/*")

        analysisfile = open("analysis.csv", "a")

        analysisfile.write("NAME,LENGTH,BITRATE,SAMPLERATE,BPM,NBEATS,INSTR/VOICE\n")


        for dir in listdir:
            analysisfile.write(dir+ "\n")

            print("\nDirectory " + str(dir) + "................. ")
            listfiles = os.listdir(dir)

            all_beatpositions = []

            for f in listfiles:
                print("\nAnalyzing " + f + "..... ")
                output = analyse.analysisFromLocal(filepath=dir + "/" + f)
                beatposition = utils.writeFeaturesOnAnalysisFile(output, analysisfile)
                all_beatpositions.append(utils.calculateBeatsDiff(beatposition))


            utils.analyzeBeatsDiff(all_beatpositions)

            print("\nFinished Folder\n\n")
            analysisfile.write("\n")

        print("No more Folder")
        analysisfile.close()

        self.redirect("/")

    @web.asynchronous
    def post(self):
        pass



app = web.Application([

    (r'/', IndexHandler),
    #(r'/api', S3AmazonHandler),
    (r'/local',localAudioHandler),


])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()
