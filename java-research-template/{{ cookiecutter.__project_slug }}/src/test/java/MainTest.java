package {{ cookiecutter.package_name }};

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class MainTest {

    @Test
    void testMain() {
        assertEquals(2 + 2, 4);
    }
}
