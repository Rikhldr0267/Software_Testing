import com.thoughtworks.selenium.DefaultSelenium;
import com.thoughtworks.selenium.Selenium;

public class zimra {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Selenium selenium = new DefaultSelenium("localhost", 4444, "firefox", "https://mail.nitrkl.ac.in/");
		selenium.start();
		selenium.open("/");
		selenium.type("id=username", "223cs3148@nitrkl.ac.in");
		selenium.type("id=password", "DB32D43A7");
		selenium.click("css=.ZLoginButton");
		selenium.windowMaximize();
	}

}














