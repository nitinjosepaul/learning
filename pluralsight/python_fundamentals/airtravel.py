class BookingException(Exception):
    pass


class RelocationException(Exception):
    pass


class Flight:

    def __init__(self, number, aircraft):
        def _check_flight_number():
            if not (number[:2].isalpha() and number[:2].isupper()):
                raise ValueError("Invalid flight code in {}".format(number))
            if not (number[2:].isdigit() and 0 < len(number[2:]) <= 4):
                raise ValueError("Invalid route number in {}".format(number))
        _check_flight_number()
        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def _parse_seat(self, seat):
        """Parse a seat designator into a valid row and letter

        Args:
            seat: A seat designator such as '12E'

        Raises:
            ValueError: For an invalid seat number

        Returns:
            A tuple containing row(int) and letter(string)

        """
        rows, seat_letters = self._aircraft.seating_plan()

        seat_letter = seat[-1]
        if seat_letter not in seat_letters:
            raise ValueError("invalid seat_letter {}".format(seat_letter))

        message = None
        try:
            row = int(seat[:-1])
            if row not in rows:
                raise ValueError("Row number not available")
        except ValueError as e:
            message = str(e)
            row = seat[:-1]
        if message:
            raise ValueError("Invalid seat row {} : {}".format(row, message))

        return row, seat_letter

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat : A seat designator such as '12E'
            passenger : passenger name

        Raises:
            BookingException : In case seat already booked

        """
        row, seat_letter = self._parse_seat(seat)

        if self._seating[row][seat_letter] is not None:
            raise BookingException("Seat {} is already booked".format(seat))

        self._seating[row][seat_letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat

        Args:
            from_seat: Existing seat designator of the passenger
            to_seat: Seat designator to be moved to

        Raises:
            RelocationException: If relocation fails
        """
        from_row, from_seat_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_seat_letter] is None:
            raise RelocationException("Source seat {} is empty".format(from_seat))

        to_row, to_seat_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_seat_letter] is not None:
            raise RelocationException("Destination seat {} is not empty".format(to_seat))

        self._seating[to_row][to_seat_letter] = self._seating[from_row][from_seat_letter]
        self._seating[from_row][from_seat_letter] = None

    def num_available_seats(self):
        """Calculates number of available/remaining seats

        Returns:
            Number(int) of seats available
        """
        return sum(sum(1 for seat in row.values() if seat is None)
                   for row in self._seating if row is not None)

    def make_boarding_pass(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self._aircraft.model())

    def _passenger_seats(self):
        """A generator function which yields all occupied passenger names and seats
        """
        rows, letters = self._aircraft.seating_plan()
        for row in rows:
            for letter in letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, "{}{}".format(row, letter)


class Aircraft:

    def __init__(self, registration, model, rows, seats_per_row):
        self._registration = registration
        self._model = model
        self._rows = rows
        self._seats_per_row = seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._rows + 1), "ABCDEFGHJK"[:self._seats_per_row]


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
             "  Seat: {1}" \
             "  Flight: {2}" \
             "  Aircraft: {3}" \
             " |".format(passenger, seat, flight_number, aircraft)
    banner = '+' + '-' * (len(output)-2) + '+'
    border = '|' + ' ' * (len(output)-2) + '|'
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


f = Flight("BA785", Aircraft("G-EUPT", "Airbus A319", rows=22, seats_per_row=6))
f.allocate_seat('22A', 'Greeshma Saju')
f.allocate_seat('22B', 'Nitin Jose Paul')
f.allocate_seat('22D', 'Gia [Sara] Nitin')
f.allocate_seat('22E', 'Jacob Nitin')
f.make_boarding_pass(console_card_printer)

# f.relocate_passenger('22A', '22B')
# print(f.num_available_seats())