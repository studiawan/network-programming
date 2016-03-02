/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package echoclient;

/**
 *
 * @author Hudan
 */

import java.net.*;
import java.io.*;

public class EchoClient {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try {
            /*
             * variable initialization
             */
            Socket clientSocket;
            DataInputStream inputStream;
            DataOutputStream outputStream;
            String message;
            
            /*
             * create socket, preapring data output stream, send to server
             */
            clientSocket = new Socket("localhost", 5000);
            outputStream = new DataOutputStream(clientSocket.getOutputStream());
            outputStream.writeUTF("Message from client");
            
            /*
             * preparing data input stream, receive message from server, print
             */
            inputStream = new DataInputStream(clientSocket.getInputStream());
            message = inputStream.readUTF();
            System.out.println("From server: " + message);
            
            /*
             * close data output stream, data input stream, and client socket
             */
            outputStream.close();
            inputStream.close();
            clientSocket.close();
        }
        catch(IOException e) {
            System.out.println("IO exception: " + e.getMessage());
        }
    }
}
