//port 55
import java.io.*;
import java.net.*;
public class Server55{
   public static void main(String[] args){
      int port = 55;
      ServerSocket serverSocket = null;
      Socket clientSocket = null;
      BufferedReader clientInput = null;
      PrintWriter clientOutput = null;
      FileInputStream fileInputStream = null;
      BufferedOutputStream clientOutputStream = null;
      
      try{                                                                       //opened try
         /* create a server socket that listens to port 55 */
         serverSocket = new ServerSocket(port);
         System.out.println("Server is listening to port " +port);
         clientSocket = serverSocket.accept();
         System.out.println("Client connected");
         clientInput = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
         clientOutputStream = new BufferedOutputStream(clientSocket.getOutputStream());
         String requestedFileName = clientInput.readLine();
         System.out.println("Client requested file: "+requestedFileName);

         File file = new File(requestedFileName);

         if(file.exists()){                                                     //opened if
            System.out.println("File is there");
            fileInputStream = new FileInputStream(file);
            byte[] buffer = new byte[1024];
            int bytesRead;
            
            while((bytesRead = fileInputStream.read(buffer)) != -1 ){           //opened while
               clientOutputStream.write(buffer,0,bytesRead);
            }                                                                  //closed while

            clientOutputStream.flush();
            System.out.println("File sent to client");
         } else {                                                              //closed if opened else
            System.out.println("Requested File doesn't exist");
         }                                                                     //closed else
      }                                                                        //closed try
      catch(IOException e){                                                    //opened catch
         e.printStackTrace();
      }                                                                        //closed catch
      finally{                                                                 //opened finally
         try{                                                                  //opened try 
            if(fileInputStream != null)
               fileInputStream.close();
            if(clientInput != null)
               clientInput.close();
            if(clientOutputStream != null)
               clientOutputStream.close();
            if(clientSocket != null)
               clientSocket.close();
            if(serverSocket != null)
               serverSocket.close();
         } catch(IOException e){                                             //closed try opened catch
         e.printStackTrace();
         }                                                                      //closed catch
      }                                                                //closed finally 
   }                                               //closed main
}                                                                  //closed class