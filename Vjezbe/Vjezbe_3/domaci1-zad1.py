import particle

p = particle.Particle()
p.set_initial_conditions(1, 0, 0, 45)

p.velocity_to_hit_target(45, 5, 1, 1)
p.velocity_to_hit_target(45, 0.5, 10, 1)
        
p.angle_to_hit_target(10, 0.5, 5, 1)



