#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os.path


def add_flight(flights, destination, departure_date, aircraft_type):

    flights.append(
        {
            "name": name,
            "знак зодиака": post,
            "year": year,
        }
    )

    return flights


def display_flights(flights):

    if flights:
        line = "+-{}-+-{}-+-{}-+-{}-+".format(
            "-" * 4, "-" * 30, "-" * 20, "-" * 8
        )
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^8} |".format(
                "No", "Name", "знак зодиака ", "year"
            )
        )
        print(line)
        for idx, flight in enumerate(flights, 1):
            print(
                "| {:>4} | {:<30} | {:<20} | {:>8} |".format(
                    idx,
                    flight.get("name", ""),
                    flight.get("знак зодиака", ""),
                    flight.get("year", ""),
                )
            )
            print(line)
    else:
        print("List of flights is empty.")


def select_flights(flights, date):

    result = []
    for flight in flights:
        if flight.get("year") == date:
            result.append(flight)
    return result


def save_flights(file_name, flights):

    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(flights, fout, ensure_ascii=False, indent=4)


def load_flights(file_name):

    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main(command_line=None):
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename", action="store", help="The data file name"
    )

    parser = argparse.ArgumentParser("flights")
    parser.add_argument(
        "--version", action="version", version="%(prog)s 0.1.0"
    )
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser(
        "add", parents=[file_parser], help="Add a new flight"
    )
    add.add_argument(
        "-d",
        "--name",
        action="store",
        required=True,
        help="name of the flight",
    )
    add.add_argument(
        "-dd",
        "--знак зодиака",
        action="store",
        required=True,
        help="Departure date of the flight",
    )
    add.add_argument(
        "-at",
        "--year",
        action="store",
        required=True,
        help="Aircraft type of the flight",
    )

    _ = subparsers.add_parser(
        "display", parents=[file_parser], help="Display all flights"
    )

    select = subparsers.add_parser(
        "select",
        parents=[file_parser],
        help="Select flights by departure date",
    )
    select.add_argument(
        "-D",
        "--date",
        action="store",
        required=True,
        help="Departure date to select flights",
    )

    args = parser.parse_args(command_line)

    is_dirty = False
    if os.path.exists(args.filename):
        flights = load_flights(args.filename)
    else:
        flights = []

    if args.command == "add":
        flights = add_flight(
            flights, args.destination, args.departure_date, args.aircraft_type
        )
        is_dirty = True

    elif args.command == "display":
        display_flights(flights)

    elif args.command == "select":
        selected = select_flights(flights, args.date)
        display_flights(selected)

    if is_dirty:
        save_flights(args.filename, flights)


if __name__ == "__main__":
    main()