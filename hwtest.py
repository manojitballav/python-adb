from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device

class hwtest(base_test.BaseTestClass):
    def setup_class(self):
        self.ads = self.register_controller(android_device)
        self.dut  = self.ads[0]
        self.dut.load_snippet('mbs','com.google.android.mobly.snippet.bundled')
    
    def test_hello(self):
        self.dub.mbs.makeToast('Mono')

if __name__ == '__main__':
    test_runner.main()
