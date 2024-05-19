#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os.path

import click


@click.group()
@click.version_option(version="0.1.0")
def flights():
    """
    Manage flight data.
    """
    pass


@flights.command()
@click.option(
    "-f", "--filename", default="rrm.json", help="The data file name"
)
@click.option(
    "-d",
    "--name ",
    prompt="name ",
    help="name  of the flight",
)
@click.option(
    "-dd",
    "--знак зодиака",
    prompt="post Date",
    help="post date of the flight",
)
@click.option(
    "-at",
    "--year",
    prompt="year Type",
    help="year type of the flight",
)
def add(filename, name, post, year):
    """
    Add a new flight.
    """
    flights = load_flights(filename)
    flights.append(
        {
            "name": name,
            "знак зодиака": post,
            "year": year,
        }
    )
    save_flights(filename, flights)


@flights.command()
@click.option(
    "-f", "--filename", default="rrm.json", help="The data file name"
)
def display(filename):
    """
    Display all flights.
    """
    flights = load_flights(filename)
    display_flights(flights)


@flights.command()
@click.option(
    "-f", "--filename", default="rrm.json", help="The data file name"
)
@click.option(
    "-at",
    "--year",
    prompt="year Type",
    help="year type to select flights",
)
def select(filename, year):
    """
    Select flights by aircraft type.
    """
    flights = load_flights(filename)
    selected = select_flights(flights, year)
    display_flights(selected)


def add_flight(flights, name, post, year):
    """
    Add flight data.
    """
    flights.append(
        {
            "name": name,
            "знак зодиака": post,
            "year": year,
        }
    )
    return flights


def display_flights(flights):
    """
    Display list of flights.
    """
    if flights:
        line = "+-{}-+-{}-+-{}-+-{}-+".format(
            "-" * 4, "-" * 30, "-" * 20, "-" * 8
        )
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^8} |".format(
                "No", "name", "знак зодиака", "year"
            )
        )
        print(line)
        for idx, flight in enumerate(flights, 1):
            print(
                "| {:>4} | {:<30} | {:<20} | {:>8} |".format(
                    idx,
                    flight.get("name", ""),
                    flight.get("year", ""),
                    flight.get("year", ""),
                )
            )
            print(line)
    else:
        print("List of flights is empty.")


def select_flights(flights, year):
    """
    Select flights by aircraft type.
    """
    result = []
    for flight in flights:
        if flight.get("знак зодиака") == year:
            result.append(flight)
    return result


def save_flights(file_name, flights):
    """
    Save all flights to a JSON file.
    """
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(flights, fout, ensure_ascii=False, indent=4)


def load_flights(file_name):
    """
    Load all flights from a JSON file.
    """
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as fin:
            return json.load(fin)
    else:
        return []


if __name__ == "__main__":
    flights()