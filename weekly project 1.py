# Daily Task Organizer
print("=== DAILY TASK ORGANIZER ===")
print()

# Pre-defined daily checklist
checklist = [
    "Workout",
    "Yoga", 
    "Morning Study",
    "Python Practice",
    "Evening Study",
    "Assignments",
    "Night Walk"
]

# Pre-organized tasks based on completion status
completed_tasks = [
    "Workout",
    "Morning Study", 
    "Python Practice",
    "Assignments"
]

incomplete_tasks = [
    "Yoga",
    "Evening Study",
    "Night Walk"
]

print("✅ Your checklist for today:")
for i, task in enumerate(checklist, 1):
    print(f"{i}. {task}")

print()
print("-" * 40)
print("🌅 END OF DAY REVIEW")
print("-" * 40)

print()
print("=" * 50)
print("📊 DAILY TASK SUMMARY")
print("=" * 50)

# Display completed tasks
print("✅ COMPLETED TASKS:")
if completed_tasks:
    for i, task in enumerate(completed_tasks, 1):
        print(f"   {i}. {task}")
else:
    print("   No tasks completed today.")

print()

# Display incomplete tasks
print("❌ INCOMPLETE TASKS:")
if incomplete_tasks:
    for i, task in enumerate(incomplete_tasks, 1):
        print(f"   {i}. {task}")
else:
    print("   All tasks completed! Great job!")

print()

# Show statistics
total_tasks = len(checklist)
completed_count = len(completed_tasks)
incomplete_count = len(incomplete_tasks)

if total_tasks > 0:
    completion_rate = (completed_count / total_tasks) * 100
    print(f"📈 STATISTICS:")
    print(f"   Total tasks: {total_tasks}")
    print(f"   Completed: {completed_count}")
    print(f"   Incomplete: {incomplete_count}")
    print(f"   Completion rate: {completion_rate:.1f}%")

print()
print("🎯 Keep up the good work! Incomplete tasks can be moved to tomorrow's list.")
print("=" * 50)

# Show task status for verification
print()
print("📋 TASK STATUS BREAKDOWN:")
print("Completed:")
for task in completed_tasks:
    print(f"   ✓ {task}")
print("Incomplete:")
for task in incomplete_tasks:
    print(f"   ✗ {task}")