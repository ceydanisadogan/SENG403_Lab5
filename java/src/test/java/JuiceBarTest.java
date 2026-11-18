// Tests for the JuiceBar order price. Run:  mvn -q test
// You add your own tests at the end of this file, under YOUR TESTS.
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

class JuiceBarTest {

    // ------------------------------------------------------------------
    // The team's tests. They all pass.
    // Do not delete them. You may make one of them stronger in Part C.
    // ------------------------------------------------------------------
    @Test
    void teamBottlePrice() {
        assertEquals(40, JuiceBar.bottlePrice("S"));
    }

    @Test
    void teamTwoSmall() {
        assertEquals(80, JuiceBar.orderPrice(2, "S", false, false));
    }

    @Test
    void teamFiveSmall() {
        assertEquals(200, JuiceBar.orderPrice(5, "S", false, false));
    }

    @Test
    void teamBigOrder() {
        assertEquals(430, JuiceBar.orderPrice(12, "S", false, false));
    }

    @Test
    void teamMemberOrder() {
        int price = JuiceBar.orderPrice(3, "S", true, false);
        System.out.println("member price: " + price);
    }

    // ------------------------------------------------------------------
    // YOUR TESTS (Part B and Part C). Write the expected value from the
    // SPECIFICATION (worksheet, step A0), not from the code.
    // The input of a test can come from the code. The expected value must
    // always come from the specification.
    // ------------------------------------------------------------------

    // This is an example of a normal test. Replace the dots with real values.
    //
    //
    // @Test
    // void myFirst() {
    //     assertEquals(..., JuiceBar.orderPrice(..., ..., false, false));
    // }

    // This is an example of a test for an input that must raise an error.
    //
    //
    // @Test
    // void myError() {
    //     assertThrows(IllegalArgumentException.class,
    //                  () -> JuiceBar.orderPrice(..., ..., false, false));
    // }
}
