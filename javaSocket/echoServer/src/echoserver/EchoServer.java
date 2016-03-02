/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package echoserver;

/**
 *
 * @author Hudan
 */

import java.net.*;
import java.io.*;

public class EchoServer {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try {
            /*
             * variable initialization
             */
            ServerSocket serverSocket;            
            Socket clientSocket;
            DataInputStream inputStream;
            DataOutputStream outputStream;
            String message;
                        
            /*
             * create socket server, accept client, preparing input stream
             * receive message, and print to screen
             */
            serverSocket = new ServerSocket(5000);
            clientSocket = serverSocket.accept();
            inputStream = new DataInputStream(clientSocket.getInputStream());
            message = inputStream.readUTF();
            System.out.println("From client: " + message);

            /*
             * preparing output stream, send message back to client
             */
            outputStream = new DataOutputStream(clientSocket.getOutputStream());
            outputStream.writeUTF(message);

            /*
             * close input stream, output stream
             * close client socket and server socket
             */
            inputStream.close();
            outputStream.close();
            clientSocket.close();
            serverSocket.close();
        }
        catch(IOException e) {
            System.out.println("Listen: " + e.getMessage());
        }        
    }
}
