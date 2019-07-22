# python3
import heapq

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # # TODO: replace this code with a faster algorithm.
        # self.assigned_workers = [None] * len(self.jobs)
        # self.start_times = [None] * len(self.jobs)
        # next_free_time = [0] * self.num_workers
        # for i in range(len(self.jobs)):
        #   next_worker = 0
        #   for j in range(self.num_workers):
        #     if next_free_time[j] < next_free_time[next_worker]:
        #       next_worker = j
        #   self.assigned_workers[i] = next_worker
        #   self.start_times[i] = next_free_time[next_worker]
        #   next_free_time[next_worker] += self.jobs[i]
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self.make_heap()
        for i in range(len(self.jobs)):
            worker = heapq.heappop(self.heap)
            load, idx = worker
            self.assigned_workers[i] = idx
            self.start_times[i] = load
            load += self.jobs[i]
            heapq.heappush(self.heap, [load, idx])

    def make_heap(self):
        self.heap = [[0,i] for i in range(self.num_workers)]
        heapq.heapify(self.heap)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

