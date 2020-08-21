import javax.swing.JFrame;
import javax.swing.JPanel;
import java.nio.file.Files;
import java.io.*;
import java.math.BigInteger;
import java.util.Scanner;

public class AudTest
{
	public static String b="";
	public  static void convert(BigInteger num)
	{
		b+= num.toString(2);
	}

	public static void main(String[] args) {

		try {

		    byte[] audInByte;
			BufferedInputStream in = new BufferedInputStream(new FileInputStream("aud.wav"));
		    ByteArrayOutputStream baos = new ByteArrayOutputStream();
			int read;
			byte[] buff = new byte[1024];
			while ((read = in.read(buff)) > 0)
			{
					baos.write(buff, 0, read);
			}

		    baos.flush();
		    audInByte = baos.toByteArray();
			BigInteger a= BigInteger.valueOf(1);

			PrintWriter writer = new PrintWriter("audioop.txt", "UTF-8");
			for(byte b:baos.toByteArray())
			{
				baos.write(b);
				writer.println(java.lang.Math.abs(b));
			}
		writer.close();
	//System.out.println(imageInByte);
        baos.close();
			//System.out.println(a);
			//writer.println(a);
			//writer.close();
		}
		catch (IOException e) {
		    System.out.println(e.getMessage());
		}
	}
}
