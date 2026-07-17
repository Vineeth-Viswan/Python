def hanoi_solver(total_disks):
	if not isinstance(total_disks, int) or total_disks < 1:
		raise ValueError("total_disks must be a positive integer")

	source = list(range(total_disks, 0, -1))
	auxiliary = []
	target = []

	states = [f"{source} {auxiliary} {target}"]

	def move(disks, start, end, spare):
		if disks == 1:
			end.append(start.pop())
			states.append(f"{source} {auxiliary} {target}")
			return

		move(disks - 1, start, spare, end)
		end.append(start.pop())
		states.append(f"{source} {auxiliary} {target}")
		move(disks - 1, spare, end, start)

	move(total_disks, source, target, auxiliary)
	return "\n".join(states)
