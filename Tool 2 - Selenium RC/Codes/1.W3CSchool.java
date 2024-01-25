import com.thoughtworks.selenium.DefaultSelenium;
import com.thoughtworks.selenium.Selenium;


public class W3CSchool {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Selenium selenium = new DefaultSelenium("localhost",4444,"firefox","https://www.w3schools.com/");
		selenium.start();
		selenium.open("/");
		selenium.windowMaximize();
		
	}

}


