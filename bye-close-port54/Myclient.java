import java.io.*;
import java.net.*;

public class Myclient {
    public static void main(String[] args) {
        try {
            // Establish connection to the server
            Socket s = new Socket("localhost", 1010);

            // Create input and output streams
            DataInputStream dis = new DataInputStream(s.getInputStream());
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());

            // BufferedReader to read input from the console
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            String str2 = "";

            // Keep communicating until the user types "bye"
            while (!str2.equals("bye")) {
                // Read user input
                String str1 = br.readLine();

                // Send message to the server
                dout.writeUTF(str1);

                // Read the server's response
                str2 = dis.readUTF();

                // Display the server's response
                System.out.println("SERVER: " + str2);
            }

            // Close the resources after the communication ends
            s.close();
            dis.close();
            dout.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
