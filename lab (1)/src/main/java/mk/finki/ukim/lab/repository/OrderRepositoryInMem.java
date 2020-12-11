package mk.finki.ukim.lab.repository;

import mk.finki.ukim.lab.database.Dataholder;
import mk.finki.ukim.lab.model.Order;
import mk.finki.ukim.lab.model.User;
import org.springframework.stereotype.Repository;

import javax.xml.crypto.Data;
import java.util.List;
import java.util.stream.Collectors;

@Repository
public class OrderRepositoryInMem {
    public List<Order> listByNameAndAddress(String clientName, String clientAddress) {
        return Dataholder.ordersList.stream()
                .filter(o -> o.getUser().getUsername().equals(clientName))
                .collect(Collectors.toList());
    }

    public Order addOrder(String balloonColor, User user) {
        Order order = new Order(balloonColor, balloonColor + " balloon", user);
        Dataholder.ordersList.add(order);
        return order;
    }
}
