package mk.finki.ukim.lab.repository;

import mk.finki.ukim.lab.database.Dataholder;
import mk.finki.ukim.lab.model.Manufacturer;
import org.apache.naming.factory.DataSourceLinkFactory;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;
import java.util.Optional;

@Repository
public class ManufacturerRepositoryInMem {
    public List<Manufacturer> findAll() {
        return Dataholder.manufacturers;
    }

    public Optional<Manufacturer> findById(Long id) {
        return Dataholder.manufacturers.stream().filter(
                b -> b.getId().equals(id)).findFirst();
    }
}

