import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.OutputStream;
import java.io.InputStream;
import java.io.ByteArrayOutputStream;
import java.io.ByteArrayInputStream;
import java.io.IOException; 
import java.nio.file.Files;
import javax.imageio.ImageIO;
import java.io.File;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.io.PrintWriter;
import java.io.Writer;
import java.lang.Object;
public class ImageTest {
public static String b="";
public  static void convert(int num)
{
	while(num!=0)
	{
		if(num%2==1)
			b+='1';
		else if(num%2==0)
			b+='0';
		num=num/2;
	}
}

public static void main(String[] args) {

    try {

        byte[] imageInByte;
        BufferedImage originalImage = ImageIO.read(new File("live.jpg"));
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ImageIO.write(originalImage, "jpg", baos);
        baos.flush();
        imageInByte = baos.toByteArray();
	int a=0;

	PrintWriter writer=new PrintWriter("imagejava.txt","UTF-8");
	for(byte b:baos.toByteArray())
	{
		baos.write(b);
		//convert(java.lang.Math.abs(b));
	writer.println(java.lang.Math.abs(b));
	}
	writer.close();
	//System.out.println(imageInByte);
        baos.close();
        /*InputStream in = new ByteArrayInputStream(imageInByte);
        BufferedImage bImageFromConvert = ImageIO.read(in);

        ImageIO.write(bImageFromConvert, "jpg", new File("op.jpg"));
*/
    } catch (IOException e) {
        System.out.println(e.getMessage());
    }
}
}
