#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

class FilterMean:
    def __init__(self, max_points=10):
        self.vals = []
        self.N = 0
        self.max_points = max_points

    def insert(self, new_val):
        if self.N < self.max_points:
            self.vals.append(new_val)
            self.N += 1
        else:
            self.vals = self.vals[1:] + [new_val]
        print(self.vals)

    def set_points(self, max_points=10):
        self.max_points = max_points
        if max_points < len(self.vals):
            self.vals = self.vals[:max_points]
            self.N = max_points

    def get_mean(self):
        return sum(self.vals)/self.N


class IntervalTimer:
    def __init__(self, timer_interval):
        self.interval = timer_interval
        self.start()

    def set_interval(self, new_interval):
        self.interval = new_interval
        self.start()

    def start(self):
        self.start_time = time.time()

    def get_passed(self):
        current_time = time.time()
        return current_time - self.start_time

    def is_done(self):
        if self.get_passed() >= self.interval:
            self.start()
            return True

        return False