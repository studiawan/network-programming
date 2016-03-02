/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package echoservermulticlient;

/**
 *
 * @author Hudan
 */

import java.net.*;
import java.io.*;

public class EchoServerMulticlient {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try {
            ServerSocket serverSocket;
            Socket clientSocket;
            
            serverSocket = new ServerSocket(5000);
            while(true) {
                clientSocket = serverSocket.accept();            
                Connection c = new Connection(clientSocket);                
            }
        }
        catch(IOException ex) {
            System.out.println("IO: " + ex.getMessage());
        }        
    }
}

class Connection extends Thread {
    DataInputStream inputStream;
    DataOutputStream outputStream;
    Socket clientSocket;
    
    public Connection(Socket client) {
        try {
            clientSocket = client;
            inputStream = new DataInputStream(clientSocket.getInputStream());
            outputStream = new DataOutputStream(clientSocket.getOutputStream());            
            this.start();
        }
        catch(IOException ex) {
            System.out.println("IO: " + ex.getMessage());
        }        
    }
    
    @Override
    public void run() {
        try {
            String message = inputStream.readUTF();            
            System.out.println("From client: " + message);            
            outputStream.writeUTF(message);                        
        }
        catch(IOException ex) {
            System.out.println(ex.getMessage());
        }
        finally {
            try {
                clientSocket.close();
            } catch (IOException ex) {
                System.out.println(ex.getMessage());
            }
        }
    }
}