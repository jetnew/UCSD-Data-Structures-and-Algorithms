# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        arrived_at, time_to_process = request

        # Update buffer at time = arrived_at
        self.update_buffer(arrived_at)
        # print("Buffer:", self.finish_time)

        # If Buffer is full, drop Response
        if self.is_full():
            return Response(True, -1)

        # If Buffer not full, add Reponse to buffer
        run_time = self.add_to_buffer(request)
        return Response(False, run_time)

    def is_full(self):
        return len(self.finish_time) == self.size

    def add_to_buffer(self, request):
        arrived_at, time_to_process = request
        if self.finish_time and arrived_at < self.finish_time[-1]:
            run_time = self.finish_time[-1]
        else:
            run_time = arrived_at
        finish_time = run_time + time_to_process
        self.finish_time.append(finish_time)
        return run_time

    def update_buffer(self, time):
        if self.is_full():
            self.finish_time = [t for t in self.finish_time if t > time]


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
