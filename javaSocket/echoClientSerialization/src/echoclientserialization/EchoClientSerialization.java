/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package echoclientserialization;

/**
 *
 * @author Hudan
 */

import messageserialization.Message;
import java.net.*;
import java.io.*;

public class EchoClientSerialization {

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
            ObjectInputStream inputStream;
            ObjectOutputStream outputStream;            
            Message message;
            
            /*
             * create socket, preparing object output stream, send object to server
             */
            clientSocket = new Socket("localhost", 5000);
            outputStream = new ObjectOutputStream(clientSocket.getOutputStream());
            outputStream.writeObject(new Message("Test from client", 1));
            outputStream.flush();
            
            /*
             * preparing object input stream, receive message from server, print
             */
            inputStream = new ObjectInputStream(clientSocket.getInputStream());
            try {
                message = (Message) inputStream.readObject();
                System.out.println("From server: " + message.getString() + " " + message.getInteger());
            } catch (ClassNotFoundException ex) {
                System.out.println("ClassNotFound: " + ex.getMessage());
            }                                    
            
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
