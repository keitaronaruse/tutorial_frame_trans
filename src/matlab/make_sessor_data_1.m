%
% @file make_sessor_data_1.m
% @author Keitaro Naruse
% @date 2024-09-09
% @brief Making sensor data
%

% NX = 600; NY = 480;
% occupancy_grid = zeros( NX, NY );
% occupancy_grid( 1:360, 240:480 ) = 1;
% occupancy_grid( 480:NX, 240:480 ) = 1;
% occupancy_grid( 1:NX, 1:120 ) = 1;
NX = 6000; NY = 4800;
occupancy_grid( 1:3600, 2400:4800 ) = 1;
occupancy_grid( 4800:NX, 2400:4800 ) = 1;
occupancy_grid( 1:NX, 1:1200 ) = 1;

num_obstacle = 0;
for i = 1:NX
    for j = 1:NY
        if occupancy_grid( i, j ) == 1
            num_obstacle = num_obstacle + 1;
        end
    end
end

disp( num_obstacle );
occupancy_list = zeros( 2, num_obstacle );
k = 1;
for i = 1:NX
    for j = 1:NY
        if occupancy_grid( i, j ) == 1
            occupancy_list( :, k ) = [ i; j ];
            k = k + 1;
       end
    end
end

% robot_trajectory = [];
% for x = 60:10:360
%     robot_trajectory = [ robot_trajectory, [ x; 180; 0 ] ];
% end
% for q = 0:10:90
%     robot_trajectory = [ robot_trajectory, [360 + 60*cos( deg2rad(q-90)); 240 + 60 * sin(deg2rad(q-90)); q] ];
% end
% for y = 240:10:420
%     robot_trajectory = [ robot_trajectory, [ 420; y; 90] ];
% end

robot_trajectory = [];
for x = 600:100:3600
    robot_trajectory = [ robot_trajectory, [ x; 1800; 0 ] ];
end
for q = 0:10:90
    robot_trajectory = [ robot_trajectory, [3600 + 600*cos( deg2rad(q-90)); 2400 + 600 * sin(deg2rad(q-90)); q] ];
end
for y = 2400:100:4200
    robot_trajectory = [ robot_trajectory, [ 4200; y; 90] ];
end

figure( 1 );
hold on;
scatter( occupancy_list( 1, : ), occupancy_list( 2, : ),  'b');
plot( robot_trajectory( 1, : ), robot_trajectory( 2, : ), 'ko-' );
hold off;
xlim( [ 1, NX ] );
ylim( [ 1, NY ] );
daspect( [ 1, 1, 1 ] );

delete( 'log1.txt' );
s = size( robot_trajectory );
writematrix( s( 2 ), 'log1.txt', 'WriteMode', 'append', 'Delimiter', ' ' );
for i = 1:s( 2 )
    x = floor( robot_trajectory( 1, i ) );
    y = floor( robot_trajectory( 2, i ) );
    q = robot_trajectory( 3, i );
    state = [ x, y, q ];
    writematrix( state, 'log1.txt', 'WriteMode', 'append', 'Delimiter', ' ' );
    
    measurement = [];
    for r = 0:10:350
        for d = 1:1000
            u = floor( x + d * cos( deg2rad( q + r ) ) );
            v = floor( y + d * sin( deg2rad( q + r ) ) );
            if 1 <= u && u <= NX && 1 <= v && v <= NY
                if occupancy_grid( u, v ) == 1
                    break
                end
            end
        end
        if d == 1000
            d = -1;
        end
        measurement = [ measurement, [ r; d ] ];
    end
    s = size( measurement );
    writematrix( s( 2 ), 'log1.txt', 'WriteMode', 'append', 'Delimiter', ' ' );
    writematrix( measurement, 'log1.txt', 'WriteMode', 'append', 'Delimiter', ' ' );
end
