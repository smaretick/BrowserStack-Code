<?php
    
    require_once('vendor/autoload.php');
    use Facebook\WebDriver\Remote\RemoteWebDriver;
    use Facebook\WebDriver\WebDriverBy;
    
    $caps = array(
                  "browser" => "Firefox",
                  "browser_version" => "62.0 beta",
                  "os" => "OS X",
                  "os_version" => "Sierra",
                  "resolution" => "1024x768",
                  "browserstack.debug" => "true"
                  );
    $web_driver = RemoteWebDriver::create(
                                          "https://smaretick3:gqzxib7a1Gwg8bbNAyNm@hub-cloud.browserstack.com/wd/hub",
                                          $caps
                                          );
    $web_driver->get("http://google.com");
    print $web_driver->getTitle();
    $web_driver->quit();
    ?>
