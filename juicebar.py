"""JuiceBar order price."""

SMALL = 40
LARGE = 60
BULK_OFF = 50
MEMBER_OFF = 15


def bottle_price(size):
    """Price in TL of one bottle of the given size."""
    if size == "S":
        return SMALL
    if size == "L":
        return LARGE
    raise ValueError("unknown size")


def order_price(qty, size, member=False, coupon=False):
    """Price in TL of an order of qty bottles of one size."""
    if qty < 1 or qty > 20:
        raise ValueError("quantity must be 1 to 20")

    price = qty * bottle_price(size)

    if qty >= 10:
        price -= BULK_OFF
        
    if coupon:
        price -= price * 0.10

    if member:
        price -= MEMBER_OFF

    return price
