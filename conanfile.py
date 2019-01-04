from conans import ConanFile


class TimerRunConan(ConanFile):
    name = "TimerRun"
    version = "1.0"
    description = "Executable Binary for Poco-Timer"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "compiler_args"
    requires = "Poco/1.8.0.1@pocoproject/stable"

    def source(self):
        self.run("git clone https://github.com/xingao0803/demo-poco-timerrun.git")

    def build(self):
        self.run("g++ demo-poco-timerrun/src/*.cpp @conanbuildinfo.args -o timerrun")

    def package(self):
        self.copy("*timerrun", dst="bin", keep_path=False)

