#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import tkinter as tk
import numpy as np

from user_interface.constants import COLOR

class GraphMainFrame(tk.Frame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg=COLOR['white'],
        )

        self.description = 'Move the points on the graph to set the relationship ' + \
            'between the ambient brightness(%) and screen brightness(%).\n\n' + \
            'The line shows the screen brightness value(%) for every ambient brightness value(%).'

        self.bind('<Enter>', self.set_description)
        self.bind('<Leave>', self.remove_description)

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__init_widgets()

    def __init_widgets(self):
        self.graph_input_frame = GraphInputFrame(self, self.controller)
        self.graph_input_frame.grid(column=0, row=0)

    def set_description(self, event):
        self.controller.set_setting_description(True, self.description, '')

    def remove_description(self, event):
        self.controller.remove_setting_description()


class GraphInputFrame(tk.Frame):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        super().__init__(
            master,
            bg=COLOR['dark_gray_2'],
            height=270,
            width=320,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.__init_widgets()

    def __init_widgets(self):
        self.graph_canvas = GraphCanvas(self, self.controller)
        self.graph_canvas.grid(column=0, row=0, sticky='n', pady=(24, 0))

        self.top_variable = tk.StringVar()
        self.top_label = tk.Label(
            self,
            font=('Bahnschrift', 9),
            textvariable=self.top_variable,
            justify='center',
            anchor='s',

            width=5,
            height=1,

            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        self.top_variable.set('0 %')
        self.top_label.place(in_=self.graph_canvas, x=0, y=0, anchor='sw')

        self.left_variable = tk.StringVar()
        self.left_label = tk.Label(
            self,
            font=('Bahnschrift', 9),
            textvariable=self.left_variable,
            justify='right',
            anchor='e',

            width=5,
            height=1,

            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        self.left_variable.set('0 %')
        self.left_label.place(in_=self.graph_canvas, x=0, y=200, anchor='se')

        self.bottom_variable = tk.StringVar()
        self.bottom_label = tk.Label(
            self,
            font=('Bahnschrift', 9),
            textvariable=self.bottom_variable,
            justify='center',
            anchor='n',

            width=5,
            height=1,

            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        self.bottom_variable.set('0 %')
        self.bottom_label.place(in_=self.graph_canvas, x=0, y=200)

        self.right_variable = tk.StringVar()
        self.right_label = tk.Label(
            self,
            font=('Bahnschrift', 9),
            textvariable=self.right_variable,
            justify='left',
            anchor='w',

            width=5,
            height=1,

            bg=COLOR['dark_gray_2'],
            fg=COLOR['white'],
        )
        self.right_variable.set('0 %')
        self.right_label.place(in_=self.graph_canvas, x=200, y=200, anchor='sw')


        self.label_image_x = tk.PhotoImage(file=os.path.abspath(__file__+'/../../../../assets/label_x.png'))
        graph_label_x = tk.Label(
            self,
            background=COLOR['dark_gray_2'],
            image=self.label_image_x,
            width=200,
            height=20,
        )
        graph_label_x.place(in_=self.graph_canvas, relx=0.5, y=224, anchor='n')

        self.label_image_y1 = tk.PhotoImage(file=os.path.abspath(__file__+'/../../../../assets/label_y1.png'))
        graph_label_y1 = tk.Label(
            self,
            background=COLOR['dark_gray_2'],
            image=self.label_image_y1,
            width=20,
            height=200,
        )
        graph_label_y1.place(in_=self.graph_canvas, x=-40, rely=0.5, anchor='e')

        self.label_image_y2 = tk.PhotoImage(file=os.path.abspath(__file__+'/../../../../assets/label_y2.png'))
        graph_label_y2 = tk.Label(
            self,
            background=COLOR['dark_gray_2'],
            image=self.label_image_y2,
            width=20,
            height=200,
        )
        graph_label_y2.place(in_=self.graph_canvas, x=240, rely=0.5, anchor='w')

    def update_labels(self, points):
        point_1x = self.graph_canvas.coords(points[0])[0] + self.graph_canvas.point_radius
        point_1y = self.graph_canvas.coords(points[0])[1] + self.graph_canvas.point_radius
        point_2x = self.graph_canvas.coords(points[1])[0] + self.graph_canvas.point_radius
        point_2y = self.graph_canvas.coords(points[1])[1] + self.graph_canvas.point_radius

        ambient_1 = round(point_1x / 2)
        screen_1 = 100 - round(point_1y / 2)
        ambient_2 = round(point_2x / 2)
        screen_2 = 100 - round(point_2y / 2)

        self.bottom_variable.set(f'{ambient_1} %')
        self.left_variable.set(f'{screen_1} %')
        self.top_variable.set(f'{ambient_2} %')
        self.right_variable.set(f'{screen_2} %')

        self.bottom_label.place_configure(x=np.interp([point_1x], [0.0, 200.0], [0.0, 154.0])[0])
        self.left_label.place_configure(y=np.interp([point_1y], [0.0, 200.0], [24.0, 200.0])[0])
        self.top_label.place_configure(x=np.interp([point_2x], [0.0, 200.0], [0.0, 154.0])[0])
        self.right_label.place_configure(y=np.interp([point_2y], [0.0, 200.0], [24.0, 200.0])[0])


class GraphCanvas(tk.Canvas):
    def __init__(self, master, controller):
        self.parent = master
        self.controller = controller
        self.width=200
        self.height=200
        super().__init__(
            master,
            bg=COLOR['dark_gray_3'],
            highlightthickness=0,

            width=self.width,
            height=self.height,
            bd=0,
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_grid_lines()


        self.point_radius = 10
        pos_1 = [0, self.height]
        pos_2 = [self.width, 0]

        # drag data is used to keep track of an item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        self.points = []
        self.points.append(self.create_point(pos_1[0], pos_1[1], self.point_radius))
        self.points.append(self.create_point(pos_2[0], pos_2[1], self.point_radius))
        self.tag_bind("point", "<ButtonPress-1>", self.drag_start)
        self.tag_bind("point", "<ButtonRelease-1>", self.drag_stop)
        self.tag_bind("point", "<B1-Motion>", self.drag)

        self.create_line_curve()


    def create_point(self, x, y, radius):
        return self.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            fill=COLOR['fg'],
            activefill=COLOR['hover'],
            tags=("point"),
        )

    def get_all_percentages(self):
        point_percentages = []
        for point in self.points:
            coords = self.coords(point)
            x = (coords[0] + self.point_radius) / 2
            y = 100 - (coords[1] + self.point_radius) / 2
            point_percentages.append((x, y))
        return point_percentages

    def get_point_percentages(self, point_id):
        coords = self.coords(point_id)
        x = (coords[0] + self.point_radius) / 2
        y = 100 - (coords[1] + self.point_radius) / 2
        return (x, y)

    def set_all_percentages(self, ambient_values, screen_values):
        for index, point in enumerate(self.points):
            ambient = ambient_values[index]
            screen = screen_values[index]
            x = float(ambient) * 2
            y = (100 - float(screen)) * 2
            self.set_point_position(point, x, y)

    def set_point_position(self, point_id, x, y):
        item_index = self.points.index(point_id)
        other_x = self.coords(self.points[item_index-1])[0] + self.point_radius

        item_x = self.coords(point_id)[0] + self.point_radius
        item_y = self.coords(point_id)[1] + self.point_radius

        delta_x = x - item_x
        delta_y = y - item_y

        if item_index == 0 and (item_x + delta_x >= other_x):
            delta_x = other_x - item_x + (-1.0)
        elif item_index == 1 and (item_x + delta_x <= other_x):
            delta_x = other_x - item_x + (1.0)

        self.move(point_id, delta_x, delta_y)
        self.create_line_curve()
        self.parent.update_labels(self.points)

    def __check_point_tag(self, item):
        if 'point' in self.gettags(item):
            return True

        return False

    def drag_start(self, event):
        # record the item and its location
        items = list(filter(self.__check_point_tag, self.find_closest(event.x, event.y)))
        if len(items) > 0:
            self._drag_data["item"] = items[0]
            self._drag_data["x"] = event.x
            self._drag_data["y"] = event.y

            self.parent.parent.parent.select_point(items[0])

            self.itemconfig('point', fill=COLOR['fg'], activefill=COLOR['hover'])
            self.itemconfig(items[0], fill=COLOR['highlight'], activefill=COLOR['highlight'])

            self.controller.enable_save()

    def drag_stop(self, event):
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        if self._drag_data["item"] is None:
            return

        item_index = self.points.index(self._drag_data["item"])

        item_x = self.coords(self._drag_data["item"])[0] + self.point_radius
        item_y = self.coords(self._drag_data["item"])[1] + self.point_radius

        other_x = self.coords(self.points[item_index-1])[0] + self.point_radius

        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]

        if item_index == 0:
            if (delta_x > 0 and event.x < 0) or \
               (delta_x < 0 and event.x >= other_x):
                delta_x = 0
        else:
            if (delta_x > 0 and event.x <= other_x) or \
               (delta_x < 0 and event.x >= 200):
                delta_x = 0

        if (delta_y > 0 and event.y < 0) or \
           (delta_y < 0 and event.y >= 200):
            delta_y = 0

        if item_index == 0:
            if (item_x + delta_x < 0):
                delta_x = -item_x
            elif (item_x + delta_x >= other_x):
                delta_x = other_x - item_x + (-1.0)
        else:
            if (item_x + delta_x <= other_x):
                delta_x = other_x - item_x + (1.0)
            elif (item_x + delta_x >= self.width):
                delta_x = self.width - item_x

        if (item_y + delta_y < 0):
            delta_y = -item_y
        elif (item_y + delta_y >= self.height):
            delta_y = self.height - item_y
        self.move(self._drag_data["item"], delta_x, delta_y)
        self.create_line_curve()

        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

        self.parent.update_labels(self.points)
        self.parent.parent.parent.update_entries()


    def create_grid_lines(self):
        for x in range(0, 201, 20):
            self.create_line(
                x, 0,
                x, 200,
                fill=COLOR['dark_gray_2'],
                width=2,
            )
        for y in range(0, 201, 20):
            self.create_line(
                0, y,
                200, y,
                fill=COLOR['dark_gray_2'],
                width=2,
            )

    def create_line_curve(self):
        point_count = len(self.points)
        color = COLOR['fg']

        positions = []
        for point in self.points:
            positions.append((
                self.coords(point)[0] + self.point_radius,
                self.coords(point)[1] + self.point_radius
            ))

        self.delete('lines')


        self.create_line(
            positions[0][0],
            self.height,
            positions[0][0],
            positions[0][1],
            fill='#FFC001',
            width=2,
            dash=(3,5),
            tags='lines',
        )
        self.create_line(
            positions[1][0],
            0,
            positions[1][0],
            positions[1][1],
            fill='#FFC001',
            width=2,
            dash=(3,5),
            tags='lines',
        )


        self.create_line(
            0,
            positions[0][1],
            positions[0][0],
            positions[0][1],
            fill=color,
            width=4,
            tags='lines',
        )

        for pt_index in range(0, point_count - 1):
            self.create_line(
                positions[pt_index][0],
                positions[pt_index][1],
                positions[pt_index + 1][0],
                positions[pt_index + 1][1],
                fill=color,
                width=4,
                tags='lines',
            )

        self.create_line(
            positions[point_count-1][0],
            positions[point_count-1][1],
            self.width,
            positions[point_count-1][1],
            fill=color,
            width=4,
            tags='lines',
        )

        self.tag_raise('point')