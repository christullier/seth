import java.lang.reflect.*;

class ReflectCount {
	public static void main(String [] args) {
		Hint c = new Hint();
		Field [] fields = Hint.class.getDeclaredFields();
		
		int mycycle;
		
		try {
			//fields[0].setAccessible(true);
			//fields[0].set(c, 10);
			//fields[1].setAccessible(true);
			//fields[1].set(c, 0);
			c.main(null);
			mycycle = (int) fields[0].get(c);
			System.out.println("field[0] is a " + fields[0] + " and has a value of " + mycycle);
		} catch (Exception e) {
			// do nothing
		}
		
		//for (Field field : fields)
		//	System.out.println(field);
	}
}
