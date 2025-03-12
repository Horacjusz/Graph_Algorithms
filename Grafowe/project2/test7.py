from data import runtests

def solve(N, exit_room, corridors, notes):
    from collections import defaultdict

    # Tworzenie grafu reprezentującego grobowiec
    graph = defaultdict(list)
    for a, b in corridors:
        graph[a].append(b)
        graph[b].append(a)

    # Symulacja trasy na podstawie notatek
    def simulate_route(graph, notes):
        notes = notes.split()
        current_room = exit_room  # Rozpoczynamy od komnaty z wyjściem
        visited = {current_room: 0}  # Słownik odwiedzonych komnat i liczba przejść przez nie
        path = [current_room]  # Ścieżka przejścia

        for note in notes:
            if note == "^":  # Powrót
                if len(path) < 2:  # Nie można się cofnąć, jeśli jesteśmy w komnacie wyjściowej
                    return False
                path.pop()  # Usuwamy ostatnią komnatę ze ścieżki
                current_room = path[-1]  # Cofamy się do poprzedniej komnaty
            else:
                # Idziemy do nowej komnaty lub przez już odwiedzony korytarz
                possible_next_rooms = graph[current_room]
                if note == "+":  # Nowy korytarz
                    # Szukamy nieodwiedzonej komnaty
                    for next_room in possible_next_rooms:
                        if next_room not in visited:
                            visited[next_room] = 0
                            current_room = next_room
                            path.append(current_room)
                            break
                    else:
                        # Nie znaleziono nowej komnaty do odwiedzenia
                        return False
                else:
                    # Przejście przez już odwiedzony korytarz w zgodnym kierunku
                    target_visits = int(note) + 1  # Liczba odwiedzin komnaty, do której chcemy przejść
                    for next_room in possible_next_rooms:
                        if visited.get(next_room, 0) == target_visits:
                            visited[next_room] += 1
                            current_room = next_room
                            path.append(current_room)
                            break
                    else:
                        # Nie znaleziono komnaty spełniającej warunki
                        return False

        # Sprawdzamy, czy ścieżka jest zgodna z notatkami i czy nie dotarliśmy do wyjścia
        return True

    # Wywołanie symulacji i zwrócenie wyniku
    return simulate_route(graph, notes)

# Przykładowe wywołanie z treści zadania

N,entrance,corridors,path = 6, 1, [(1, 2), (2, 3), (2, 4), (1, 5), (5, 6)], "+ ^ + ^ +"

print(solve(N,entrance,corridors,path))

runtests(solve)