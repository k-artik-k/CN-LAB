import java.io.*;
import java.net.*;

public class Client55 {
    public static void main(String[] args) {
        String serverAddress = "localhost";
        int port = 55;
        Socket socket = null;
        BufferedReader userInputReader = null;
        PrintWriter serverOutput = null;
        BufferedReader serverInput = null;
        FileOutputStream fileOutputStream = null;

        try {
            // Connect to the server
            socket = new Socket(serverAddress, port);
            System.out.println("Connected to server at " + serverAddress + ":" + port);

            // Set up I/O streams
            serverOutput = new PrintWriter(socket.getOutputStream(), true);
            serverInput = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            userInputReader = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Enter the name of the file to request: ");
            String fileName = userInputReader.readLine();

            // Send file request to server
            serverOutput.println(fileName);

            // Prepare to receive the file
            fileOutputStream = new FileOutputStream("Received_" + fileName);
            BufferedInputStream serverInputStream = new BufferedInputStream(socket.getInputStream());
            byte[] buffer = new byte[1024];
            int bytesRead;

            // Receive and save the file
            while ((bytesRead = serverInputStream.read(buffer)) != -1) {
                fileOutputStream.write(buffer, 0, bytesRead);
            }
            System.out.println("File received & saved as 'Received_" + fileName + "'.");

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                // Close all resources in finally block
                if (userInputReader != null)
                    userInputReader.close();
                if (serverOutput != null)
                    serverOutput.close();
                if (serverInput != null)
                    serverInput.close();
                if (fileOutputStream != null)
                    fileOutputStream.close();
                if (socket != null)
                    socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
