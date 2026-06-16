import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Tests for calc add() method")
public class testTest {
    private int a,b;

    @BeforeAll
    static void initAll() {
        System.out.println("Starting all tests...");
    }

    @BeforeEach
    void setUp() {
         a = 1;
         b = 2;
    }
    @Test
    void testAdd() {
        int result = test.add(a, b);
        assertEquals(result, a + b);
    }
    @Test
    void testAdd0_throw() {
        assertThrows(IllegalArgumentException.class, () -> {test.add(a,0);});
    }
    @AfterAll
    static void cleanUP() {
        System.out.println("Finished all tests...");
    }
}
