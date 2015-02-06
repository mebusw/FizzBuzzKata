FizzBuzzKata
============

### Status: http://mebusw.github.io/FizzBuzzKata/
![](https://travis-ci.org/mebusw/FizzBuzzKata.svg)

### Here is the problem description:

假如您是一个程序员，要实现一个FizzBuzz的游戏。FizzBuzz是国外小学里老师和孩子们一起玩的游戏。下课前5分钟，老师让孩子们站成一个圈，然后用手指指着第一个孩子，第一个孩子要迅速地说“1”；接着老师快速地指第二个孩子，第二个孩子要迅速说“2”；依次类推，每个被老师指到的孩子要迅速地递增报数。而且，如果孩子遇到3的倍数，就不能说数字，而要说“Fizz”；如果遇到5的倍数，则要说“Buzz”；如果既是3又是5的倍数，则要说“FizzBuzz”。说错或反应慢的孩子就不能再继续游戏。看谁能坚持一直游戏到最后。这是一个很锻炼乘法心算和反应能力的游戏。

您作为程序员，已经按照项目组里的产品需求专家累君交代的需求实现了FizzBuzz这个游戏。有一天，累君找到您，说：“咱们的CEO瞧不死在昨天跟我说，为了提升咱们这个游戏在中国市场的竞争力，考虑到中国人勤劳智慧，可以增加游戏的难度和趣味性，即当孩子遇到3的倍数时，除了说Fizz外，还要摸一下头；当说Buzz时还要摸一下肩膀；当说FizzBuzz时还要摸一下膝盖。但这些新增的功能仅仅针对中国市场。对于中国以外的市场，还是按照以前只说Fizz, Buzz和FizzBuzz来实现。”您打算用面向对象的开发方法(比如State或Strategy设计模式)来实现Business特性开关，并试图做到：无论特性开关是打开还是关闭，针对国内和国外两个市场的功能的测试都能够正常运行通过。

参考文章：
* Martin Fowler - Feature Toggle: http://martinfowler.com/bliki/FeatureToggle.html
* 路宁 - 特性开关问与答: http://www.luning.name/post/2013-01-17/feature-toggle-faq 
* 孟宇 - 在项目中透明地引入特性开关: http://www.infoq.com/cn/articles/introducing-characteristics-switch-in-project-transparently#rd?sukey=abc050baad029375fe4fc74465447381fc3dfbf0282db3b7a75428d15d780b7bbeb32fbc952743b95e8d2181132f8a8c#3970668-tsina-1-13950-4940258fac58681d93622513463cbd0b
