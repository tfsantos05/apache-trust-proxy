local lfs = require "lfs"

function append_slash(r)
    local uri = r.uri

    if r.method ~= "GET" then
        return apache2.DECLINED
    end

    -- Make sure we have a filename
    if not r.filename then
        return apache2.DECLINED
    end

    -- Check if it's a directory using LFS
    local attr = lfs.attributes(r.filename)
    if attr and attr.mode == "directory" and not uri:match("/$") then
        local host = r.headers_in["X-Forwarded-Host"] or r.headers_in["Host"]
        local port = r.headers_in["X-Forwarded-Port"] or r.server_port
        local scheme = r.headers_in["X-Forwarded-Proto"] or "http"

        local target = scheme .. "://" .. host
        if port ~= "80" and port ~= "443" then
            target = target .. ":" .. port
        end
        target = target .. uri .. "/"

        r.status = 301
        r.headers_out["Location"] = target
        return apache2.DONE
    end

    return apache2.DECLINED
end
