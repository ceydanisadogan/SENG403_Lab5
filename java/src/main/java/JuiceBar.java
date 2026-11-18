// JuiceBar order price. The specification (S1-S5) is in the worksheet, step A0.
// Do not read the tests to learn the rules. Read the specification.
public final class JuiceBar {

    static final int SMALL = 40;
    static final int LARGE = 60;
    static final int BULK_OFF = 50;
    static final int MEMBER_OFF = 15;

    private JuiceBar() { }

    /** Price in TL of one bottle of the given size. */
    static int bottlePrice(String size) {
        if (size.equals("S")) {
            return SMALL;
        }
        if (size.equals("L")) {
            return LARGE;
        }
        throw new IllegalArgumentException("unknown size");
    }

    /** Price in TL of an order of {@code qty} bottles of one size. */
    public static int orderPrice(int qty, String size, boolean member, boolean coupon) {
        if (qty < 1 || qty > 20) {
            throw new IllegalArgumentException("quantity must be 1 to 20");
        }
        int price = qty * bottlePrice(size);
        if (qty > 10) {
            price = price - BULK_OFF;
        }
        if (coupon) {
            price = price - 10;
        }
        if (member) {
            price = price - MEMBER_OFF;
        }
        return price;
    }
}
