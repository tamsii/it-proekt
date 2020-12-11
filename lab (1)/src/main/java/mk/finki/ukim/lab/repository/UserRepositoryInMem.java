package mk.finki.ukim.lab.repository;

import mk.finki.ukim.lab.database.Dataholder;
import mk.finki.ukim.lab.model.User;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public class UserRepositoryInMem {
    public Optional<User> tryLogin(String username, String password) {
        return Dataholder.users.stream().filter(i->i.getUsername().equals(username)
                && i.getPassword().equals(password)).findFirst();
    }

    public Optional<User> findByUsername(String clientName) {
        return Dataholder.users.stream().filter(i->i.getUsername().equals(clientName)).findFirst();
    }
}


