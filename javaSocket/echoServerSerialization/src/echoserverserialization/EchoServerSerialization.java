/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package echoserverserialization;

/**
 *
 * @author Hudan
 */

import messageserialization.Message;
import java.net.*;
import java.io.*;

public class EchoServerSerialization {

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
            ObjectInputStream inputStream;
            ObjectOutputStream outputStream;         
            Message message = null;
                        
            /*
             * create socket server, accept client, preparing object input stream
             * receive message, and print to screen
             */
            serverSocket = new ServerSocket(5000);
            clientSocket = serverSocket.accept();
            inputStream = new ObjectInputStream(clientSocket.getInputStream());
            try {
                message = (Message) inputStream.readObject();
                System.out.println("From client: " + message.getString() + " " + message.getInteger());                                
            } catch (ClassNotFoundException ex) {
                System.out.println("ClassNotFound: " + ex.getMessage());
            }            
            /*
            * preparing object output stream, send message back to client
            */
           outputStream = new ObjectOutputStream(clientSocket.getOutputStream());           
           outputStream.writeObject(new Message(message.getString(), message.getInteger()));                                  
           outputStream.flush();

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
