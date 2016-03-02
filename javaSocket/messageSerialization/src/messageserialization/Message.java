/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package messageserialization;

import java.io.Serializable;

/**
 *
 * @author Hudan
 */
public class Message implements Serializable {
    private String message;
    private int value;
    
    public Message(String message, int value) {
        this.message = message;
        this.value = value;
    }
    
    public String getString() {
        return message;
    }
    
    public int getInteger() {
        return value;
    }
    
}
