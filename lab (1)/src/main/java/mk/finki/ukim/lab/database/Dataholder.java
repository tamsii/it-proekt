package mk.finki.ukim.lab.database;

import mk.finki.ukim.lab.model.Balloon;
import mk.finki.ukim.lab.model.Manufacturer;
import mk.finki.ukim.lab.model.Order;
import mk.finki.ukim.lab.model.User;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Component
public class Dataholder {
    public static List<Balloon> balloons = new ArrayList<>();
    public static List<Order> ordersList = new ArrayList<>();
    public static List<Manufacturer> manufacturers = new ArrayList<>();
    public static List<User> users = new ArrayList<>();


    @PostConstruct
    public void init() {
        balloons.add(new Balloon("pink", "pink balloon"));
        balloons.add(new Balloon("red", "red balloon"));
        balloons.add(new Balloon("orange", "orange balloon"));
        balloons.add(new Balloon("yellow", "yellow balloon"));
        balloons.add(new Balloon("green", "green balloon"));
        balloons.add(new Balloon("blue", "blue balloon"));
        balloons.add(new Balloon("purple", "purple balloon"));
        balloons.add(new Balloon("brown", "brown balloon"));
        balloons.add(new Balloon("black", "black balloon"));
        balloons.add(new Balloon("gray", "gray balloon"));

        manufacturers.add(new Manufacturer("D-Company", "Germany", "DE"));
        manufacturers.add(new Manufacturer("I-Company", "Italy", "IT"));
        manufacturers.add(new Manufacturer("S-Company", "Sweden", "SW"));
        manufacturers.add(new Manufacturer("M-Company", "Macedonia", "MK"));
        manufacturers.add(new Manufacturer("E-Company", "England", "EN"));
        users.add(new User("tamara.danilovska", "tamss"));

    }

}
