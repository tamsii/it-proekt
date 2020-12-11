package mk.finki.ukim.lab.model;

import lombok.Data;

import javax.persistence.*;
import java.util.Random;

@Data
@Entity
@Table(name = "OrderApp")
public class Order {

    private String balloonColor;

    private String balloonSize;

    //private String clientName;

    //private String clientAddress;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long orderId;

    @ManyToOne
    private User user;

    public Order(String balloonColor, String balloonSize, User user) {
        this.balloonColor = balloonColor;
        this.balloonSize = balloonSize;
        this.user = user;
    }

    public Order() {
    }
}
