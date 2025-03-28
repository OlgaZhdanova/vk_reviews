import luigi

class HelloWorldTask(luigi.Task):
    def run(self):
        print('Hello world!')
if __name__ == '__main__':
    luigi.run()
    
class MyTask(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter(default=45)
    
    def run(self):
        print(self.x + self.y)
        
