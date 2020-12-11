package mk.finki.ukim.lab.service.implementations;
import mk.finki.ukim.lab.model.User;
import mk.finki.ukim.lab.model.exceptions.WrongCredentialsException;
import mk.finki.ukim.lab.repository.jpa.UserRepository;
import mk.finki.ukim.lab.service.LoginService;
import org.springframework.stereotype.Service;

@Service
public class LoginServiceImpl  implements LoginService {
    private final UserRepository repository;

    public LoginServiceImpl(UserRepository repository) {
        this.repository = repository;
    }

    @Override
    public User login(String username, String password) {
        return repository.findByUsernameAndPassword(username,password).orElseThrow(()-> new WrongCredentialsException());
    }
}
