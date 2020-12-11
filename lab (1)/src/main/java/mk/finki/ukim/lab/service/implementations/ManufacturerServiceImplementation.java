package mk.finki.ukim.lab.service.implementations;

import mk.finki.ukim.lab.model.Manufacturer;
import mk.finki.ukim.lab.repository.jpa.ManufacturerRepository;
import mk.finki.ukim.lab.service.ManufacturerService;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
@Service

public class ManufacturerServiceImplementation  implements ManufacturerService {
    private final ManufacturerRepository manufacturerRepository;

    public ManufacturerServiceImplementation(ManufacturerRepository manufacturerRepository) {
        this.manufacturerRepository = manufacturerRepository;
    }

    @Override
    public List<Manufacturer> findAll() {
        return this.manufacturerRepository.findAll();
    }

    @Override
    public Optional<Manufacturer> findById(Long id) {
        return this.manufacturerRepository.findById(id);
    }
}
