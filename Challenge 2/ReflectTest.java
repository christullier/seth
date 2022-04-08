import java.lang.reflect.*;

class ReflectTest {
	public static void main(String [] args) throws Exception {
		Hint t = new Hint();
		
		Class c = t.getClass();
		
		System.out.println("The name of the class is " + c.getName());
		
		try {
			Constructor con = c.getConstructor();
			System.out.println("The constructor is called " + con.getName());
		} catch (Exception e) {
			System.out.println("Error: no contstructor given...");
		}
		
		Method [] methods = c.getMethods();
		for (Method method : methods)
			System.out.println(method.getName());
		
		System.out.println("-------------------------------------------");
		
		Method [] allmethods = c.getDeclaredMethods();
		for (Method method : allmethods)
			System.out.println(method.getName());
		
		System.out.println("-------------------------------------------");
		
		//Method methodcall3 = c.getDeclaredMethod("method3", int.class);
		//methodcall3.invoke(t, 3);
		
		System.out.println("-------------------------------------------");
		
		Method methodcall2 = c.getDeclaredMethod("getLength");
		methodcall2.setAccessible(true);
		methodcall2.invoke(t);
	}
}
